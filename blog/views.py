from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogAllListView(ListView):
    model = Blog

    template_name = 'blog/blog_all_list.html'


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    extra_context = {
        'title': 'Создание статьи',
    }
    fields = ['title', 'body', 'preview', 'is_published']
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    extra_context = {
        'title': 'Редактирование статьи',
    }
    fields = ['title', 'body', 'preview', 'is_published']

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


def toggle_published(slug):
    blog_item = get_object_or_404(Blog, slug=slug)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True

    blog_item.save()

    return redirect(reverse('blog:blog_list'))

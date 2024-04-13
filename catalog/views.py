from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# Create your views here.

# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Список товаров'
#     }
#     return render(request, 'catalog/home.html',  context)
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name} {phone}: {message}')
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'You have new message from {name} {phone}: {message}')
        return super().get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


# def product(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Продукты'
#     }
#     return render(request, 'catalog/product.html', context)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_item.html'

# def product_item(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk)
#     }
#     return render(request, 'catalog/product_item.html', context)

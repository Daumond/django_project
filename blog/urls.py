from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, toggle_published, \
    BlogAllListView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('published/<slug:slug>/', toggle_published, name='toggle_published'),
    path('all/', BlogAllListView.as_view(), name='blog_all_list'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.utils import set_published, set_unpublished
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryListView

app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_item'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('product/<int:pk>/published', set_published, name='product_published'),
    path('product/<int:pk>/unpublished', set_unpublished, name='product_unpublished'),

    path('category/list', CategoryListView.as_view(), name='category_list'),
]

static(settings.MEDIA_URL, document_root='settings.MEDIA_ROOT')

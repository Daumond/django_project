from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import ProductListView, ProductDetailView


app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_item'),
]

static(settings.MEDIA_URL, document_root='settings.MEDIA_ROOT')

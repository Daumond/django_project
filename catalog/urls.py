from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import contacts, home, product, product_item


app_name = 'catalog'
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product, name='product'),
    path('product/<int:pk>/', product_item, name='product'),
]

static(settings.MEDIA_URL, document_root='settings.MEDIA_ROOT')

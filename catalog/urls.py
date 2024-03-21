from django.urls import path
from catalog.views import contacts, home


app_name = 'catalog'
urlpatterns = [
    path('', home),
    path('contacts/', contacts),
]

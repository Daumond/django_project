from django.contrib.auth.decorators import permission_required
from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View

from catalog.models import Product, Category


@permission_required('product.set_published')
def set_published(request, pk):
    product = Product.objects.get(pk=pk)
    product.is_published = True
    product.save()
    return redirect(reverse('catalog:product_item', kwargs={'pk': pk}))


@permission_required('product.set_published')
def set_unpublished(request, pk):
    product = Product.objects.get(pk=pk)
    product.is_published = False
    product.save()
    return redirect(reverse('catalog:product_item', kwargs={'pk': pk}))

def category_cache():
    key = 'category_list'
    category_list = cache.get(key)

    if category_list is None:
        category_list = Category.objects.all()
        cache.set(key, category_list)

    return category_list

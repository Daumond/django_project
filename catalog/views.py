from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.
def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Список товаров'
    }
    return render(request, 'catalog/home.html',  context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} {phone}: {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog/product.html', context)


"""
def product_category(request, category):
    context = {
        'object_list': Product.objects.filter(category_id=category),
    }
    return render(request, 'catalog/product.html', context)
"""
def product_item(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product_item.html', context)

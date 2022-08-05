from django.shortcuts import render
from products.models import Products

# Create your views here.

def create_product(request):
    new_product = Products.objects.create(
        type = 'Televisor',
        brand = 'Samsung',
        model = 'AU7000',
        price = 220000,
        description = '65'', 4K, UHD',
        stock = 20
    )
    context = {
        'new_product':new_product
    }
    return render(request,'new_product.html', context=context)

def list_products(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products_list.html', context=context)
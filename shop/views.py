from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

def index(request):
    return render(request, 'base.html')

def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(available=True)

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 
        'shop/product/list.html',
        {'category': category,
        'products': products})   
    

def detail(request, id, slug):
    product = Product.objects.get(
                            id=id,
                            slug=slug,
                            available=True)
    
    cart_product_form = CartAddProductForm()
    return render(request, 
        'shop/product/detail.html',
        {'product':product,
        'cart_product_form': cart_product_form})
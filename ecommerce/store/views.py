from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.

def index(request):
    all_products = Product.objects.all()
    return render(request, 'store/index.html', {'my_products':all_products})

def categories(request):
    all_categories = Category.objects.all()
    return {"all_categories":all_categories}

def product_info(request, slug):
    object = Product.objects.get(slug=slug)
    return render(request, 'store/product-info.html', {'product':object})

def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list-category.html', {'products':products, 'category':category})
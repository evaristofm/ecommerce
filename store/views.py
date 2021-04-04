from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


from .models import Category, Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('')

class ProductUpdateView(UpdateView):
    model = Product
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('')

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('')
'''
def all_products(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})
'''
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def test(request):
    return render(request, 'store/home.html', {'products': products})
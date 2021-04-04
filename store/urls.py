from django.urls import path

from .views import (
    ProductCreateView, ProductDeleteView, ProductDetailView,
    ProductListView, ProductUpdateView, test , category_list 
)

app_name = 'store'

urlpatterns = [
    path('', ProductListView.as_view(), name='all_products'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='pet-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='pet-delete'),
    path('shop/<slug:category_slug>/', category_list, name='category_list'),
    path('test', test, name='test')
]

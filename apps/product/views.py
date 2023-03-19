from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse

from apps.product.models import ProductModel

# Create your views here.
class ProductListView(ListView):
    model = ProductModel

class ProductCreateView(CreateView):
    model = ProductModel
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse('product_list')
    
class ProductDetailView(DetailView):
    model = ProductModel

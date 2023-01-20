from django.shortcuts import render
from django.views.generic.list import ListView

from apps.product.models import ProductModel

# Create your views here.
class ProductListView(ListView):
    model = ProductModel
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from apps.product.models import ProductModel

# Create your views here.
class ProductListView(ListView):
    model = ProductModel

class ProductCreateView(CreateView):
    model = ProductModel
    fields = "__all__"
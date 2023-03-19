from django.urls import path

from apps.product.views import ProductCreateView, ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view()),
    path('<str:pk>', ProductDetailView.as_view(), name='product_detail')
]
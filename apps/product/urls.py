from django.urls import path

from apps.product.views import ProductCreateView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view())
]
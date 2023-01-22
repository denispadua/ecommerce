from django.views.generic.edit import CreateView
from django.urls import reverse

from apps.user.models import UserModel

class UserCreateView(CreateView):
    model = UserModel
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse('product_list')
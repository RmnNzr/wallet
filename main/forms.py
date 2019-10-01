from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class NewForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

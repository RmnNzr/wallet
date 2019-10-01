from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from rest_framework.authtoken.models import Token


class NewForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        this_user = super(NewForm, self).save()
        this_token = Token.objects.create(user=this_user)
        print(this_token.key)
        return this_user, this_token

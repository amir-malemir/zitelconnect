from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomCreationFrom(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','phone_number','is_admin')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','phone_number','is_admin' )














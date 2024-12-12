from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm, CustomCreationFrom
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationFrom
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['is_admin', 'email', 'username', 'is_staff','phone_number']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number','is_admin')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number','is_admin')}),
    )
    

admin.site.register(CustomUser, CustomUserAdmin)


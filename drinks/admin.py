from django.contrib import admin


from .models import Drink

@admin.register(Drink)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'teamaker', 'status', 'datetime_created', 'datetime_modified')

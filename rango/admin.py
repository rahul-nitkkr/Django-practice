from django.contrib import admin
from rango.models import Category , Page
# Register your models here.

class CategoryAdmin:
    prepopulated_fields = {'slug':('name' , )}

admin.site.register(Category)
admin.site.register(Page)
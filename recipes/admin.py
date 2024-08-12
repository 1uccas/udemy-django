from django.contrib import admin

from .models import Category
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

class CategoryAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(Category, CategoryAdmin)
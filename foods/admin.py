from django.contrib import admin
from foods.models import Food, Category


class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "publisher_name"]

admin.site.register(Food,FoodAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Category,CategoryAdmin)



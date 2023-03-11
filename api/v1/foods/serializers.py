from rest_framework.serializers import ModelSerializer
from foods.models import Food
from rest_framework import serializers


class FoodSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = Food

    
    def get_category(self, instance):
        return instance.category.name


class FoodDetailSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        fields = ("id", "name", "publisher_name", "featured_image", "category", "ingredients", "description")
        model = Food


    def get_category(self, instance):
        return instance.category.name
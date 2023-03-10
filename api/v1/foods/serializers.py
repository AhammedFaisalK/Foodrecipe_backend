from rest_framework.serializers import ModelSerializer
from foods.models import Food


class FoodSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Food
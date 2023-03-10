from django.urls import path
from api.v1.foods.views import foods

urlpatterns = [
    path("",foods)
] 

from django.urls import path
from api.v1.foods.views import foods, singleFood, create

urlpatterns = [
    path("",foods),
    path("view/<int:pk>/",singleFood),
    path("create/",create),

] 

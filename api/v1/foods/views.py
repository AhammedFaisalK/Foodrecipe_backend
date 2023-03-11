from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from foods.models import Food
from api.v1.foods.serializers import FoodSerializer, FoodDetailSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def foods(request):
    instances = Food.objects.filter(is_deleted = False)

    context = {
        "request" : request
    }
    serializer = FoodSerializer(instances,many=True,context=context)
    response_data = {
        "status_code" : 6000,
        "data" : serializer.data
    }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def singleFood(request, pk):
    if Food.objects.filter(pk=pk).exists():
        instance = Food.objects.get(pk=pk)
        context = {
        "request" :  request
        }
   
        serializer = FoodDetailSerializer(instance,context=context)
        response_data = {
            "status_code" : 6000,
            "data" :  serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code" : 6001,
            "message" :  "This Food doesn't exist"
        }
        return Response(response_data) 
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = FoodSerializer(data=request.data)
        
    if serializer.is_valid():
        serializer.save()

        response_data = {
            "status_code" : 6000,
            "message" :  "Success"
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code" : 6001,
            "message" :  "Validation Error",
            "data" : serializer.errors
        }

        return Response(response_data)
    
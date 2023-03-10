from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from foods.models import Food
from api.v1.foods.serializers import FoodSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
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
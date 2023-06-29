from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aspa.models import AbstractUser,User
from aspa.serializers import UserSerializer
from rest_framework.exceptions import status,ValidationError

# Create your views here.
@api_view(['GET'])
def get(request):
    if request.query_params:
        users = User.objects.filter(**request.query_params.dict())
    else:
        users = User.objects.all()

    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def create_user(request):
    user =  UserSerializer(data=request.data)
    if User.objects.filter(**request.data).exists:
        raise ValidationError('User already exists')
    if user.is_valid():
        user.save()
        return Response (user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
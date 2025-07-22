from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema



@extend_schema(tags=['User API'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

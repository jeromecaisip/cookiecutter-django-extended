from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

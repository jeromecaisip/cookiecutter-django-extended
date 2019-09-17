from rest_framework import  serializers
from {{ cookiecutter.project_slug }}.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

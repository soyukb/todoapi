from rest_framework import serializers
from .models import ToDos

class ToDosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToDos
        fields = "__all__"
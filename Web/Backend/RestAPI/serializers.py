# myapp/serializers.py
from rest_framework import serializers
from RestAPI.models import ModelAPI ,ResultAPI

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelAPI
        fields = '__all__'
        
class MyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultAPI
        fields = '__all__'
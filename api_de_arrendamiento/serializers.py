from rest_framework import serializers
from django.contrib.auth.models import User
from .models import vehiculo, conductor, pasajero, arrendamiento


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]
        
class vehiculoSerilizer(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = '__all__'
        
class conductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = conductor
        fields = '__all__'
        
class pasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = pasajero
        fields = '__all__'
        
class arrendamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = arrendamiento
        fields = '__all__'
        

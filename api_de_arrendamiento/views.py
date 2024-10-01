from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_list_or_404, render, redirect
from rest_framework import viewsets
from .models import arrendamiento
from .serializers import arrendamientoSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.http import JsonResponse

class Api_arrendamiento(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                arrendamiento_obj = arrendamiento.objects.get(pk=pk)
                serializer = arrendamientoSerializer(arrendamiento_obj)
                return Response(serializer.data)
            except arrendamiento.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            arrendamientos = arrendamiento.objects.all()
            serializer = arrendamientoSerializer(arrendamientos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = arrendamientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            arrendamiento_obj = arrendamiento.objects.get(pk=pk)
        except arrendamiento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = arrendamientoSerializer(arrendamiento_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            arrendamiento_obj = arrendamiento.objects.get(pk=pk)
        except arrendamiento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        arrendamiento_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(["POST", "GET"])
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    user = get_list_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error": "invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    if request.content_type == 'application/json':
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)
    return redirect('arrendamientos')  # Redirige a la vista de arrendamientos

@api_view(["POST", "GET"])
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(serializer.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        if request.content_type == 'application/json':
            return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
        return redirect('login')  # Redirige a la vista de login
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

class arrendamientoViewSet(viewsets.ModelViewSet):
    queryset = arrendamiento.objects.all()
    serializer_class = arrendamientoSerializer

@login_required
def arrendamientos(request):
    arrendamientos = arrendamiento.objects.all()
    return render(request, 'arrendamientos.html', {'arrendamientos': arrendamientos})





@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

class arrendamientoViewSet(viewsets.ModelViewSet):
    queryset = arrendamiento.objects.all()
    serializer_class = arrendamientoSerializer
    
    
@login_required
def arrendamientos(request):
    arrendamientos = arrendamiento.objects.all()
    return render(request, 'arrendamientos.html',{'arrendamientos' : arrendamientos})

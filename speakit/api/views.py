from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as knoxLoginView
from django.contrib.auth.models import User
from rest_framework.views import APIView
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginApi(knoxLoginView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginApi, self).post(request, format=None)


class ValidateUsernameApi(APIView):   
    def post(self, request, *args, **kwargs):
        response = {}
        peticion = request.POST.get('json')
        data = json.loads(peticion)
        username = data['username']
        print(username)
        response['validated'] = not User.objects.filter(username=username).exists()
        return Response(response)

class Prueba(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'Hello'}
        return Response(content)

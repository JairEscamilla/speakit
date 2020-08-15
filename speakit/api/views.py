from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, PostSerializer, UsersInfoSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as knoxLoginView
from django.contrib.auth.models import User
from rest_framework.views import APIView
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from posts.models import Post
from rest_framework import filters
from django.db.models import Q
from users.models import Profile
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
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

class ValidateEmailApi(APIView):

    def post(self, request, *args, **kwargs):
        response = {}
        peticion = request.POST.get('json')
        data = json.loads(peticion)
        email = data['email']
        response['validated'] = not User.objects.filter(email=email).exists()
        return Response(response)

class GetUserIdApi(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        response = {}
        peticion = request.POST.get('json')
        data = json.loads(peticion)
        username = data['username']
        response['id'] = User.objects.filter(username=username).first().id 
        return Response(response)



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    #permission_classes = (IsAuthenticated, )


class PostByUser(generics.ListCreateAPIView):
    search_fields = ['user__username']
    filter_backends = (filters.SearchFilter, )
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer

class SearchUsers(APIView):

    def post(self, request, *args, **kwargs):
        response = {}
        peticion = request.POST.get('json')
        data = json.loads(peticion)
        user_searched = data['user']
        users = User.objects.filter(
            Q(username__icontains=user_searched) | 
            Q(first_name__icontains=user_searched) | 
            Q(last_name__icontains=user_searched)
        )

        for user in users:
            response[user.id] = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        
        return Response(response)

class GetUsersInfoApi(viewsets.ModelViewSet):
    serializer_class = UsersInfoSerializer
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated, )

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, username=pk)

        serializer = UsersInfoSerializer(user)

        return Response(serializer.data)
    

    def update(self, request, pk=None):
        user = get_object_or_404(User, username=pk)
        serializer = UsersInfoSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class Prueba(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'Hello'}
        return Response(content)

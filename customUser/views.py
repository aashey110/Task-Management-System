from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from rest_framework.exceptions import PermissionDenied


from .models import CustomUser
from .serializer import CustomUserSerializer

# Create your views here

class RegisterAPIView(APIView):

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)
        
class LoginAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_data = CustomUserSerializer(user).data
            return Response({'message': 'Login Success',  'user': user_data} )
        return Response({'message': 'Invalid Credentials'})
    

class ProfileAPIView(APIView):

    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        if user != request.user:
            raise PermissionDenied("You are not authorized to view this profile")
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
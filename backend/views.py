from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

# Create your views here.
User = get_user_model()

class AuthViewSet(viewsets.ViewSet):
    Permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        try:
            email            = request.data.get('email')
            password         = request.data.get('password')
            password_confirm = request.data.get('password_confirm')


            if not all([email,password,password_confirm]):
                return Response({'error':'All field are required'},status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(email=email).exists():
                return Response({'error':'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

            if password != password_confirm:
                return Response({'error': 'Password do not match'}, status=status.HTTP_400_BAD_REQUEST)

            if email and password:
                user = User.objects.create_user(
                    email=email,
                    password=password
                )
                return Response(
                   status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"error": "Email and password are required."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response({'error': f'Internal Server Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  



    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user:
            user = authenticate(request, email=user.email, password=password)

            if user:
                # Check if the user is active
                if user.is_active:
                    login(request, user)

                    return Response({'message': 'Login successful',}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'User is not active'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # logout method
    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)

        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)










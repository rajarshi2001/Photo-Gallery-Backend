from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data
        })

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserApi(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


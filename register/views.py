from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from .models import UserDetails, UserAddresses
from .serializers import RegistrationSerializer, UserAddressesSerializer, UserCorrespondanceAddressSerializer
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class RegistrationAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = RegistrationSerializer
    queryset = UserDetails.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'email', 'username']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success", "Message": "User created successfully", "User": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:

            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})


# creating a class to log in the user
class UserAddressesAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    permission_classes = (AllowAny,)
    serializer_class = UserAddressesSerializer
    queryset = UserAddresses.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'user_id', 'address', 'city', 'state', 'country', 'pincode']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success", "Message": "address entered successfully", "User": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:

            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    def get(self, request):
        return Response({'Status': 'You cannot view all users data.....'})


class UserCorrespondanceAddressAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    permission_classes = (AllowAny,)
    serializer_class = UserCorrespondanceAddressSerializer
    queryset = UserAddresses.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'user_id', 'city', 'state', 'country', 'pincode']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success", "Message": "corresponding address entered successfully", "User": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:

            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    def get(self, request):
        return Response({'Status': 'You cannot view all users data.....'})


class ListUserAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    queryset = UserDetails.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'email', 'username']

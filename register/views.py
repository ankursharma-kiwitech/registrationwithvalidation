from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import UserDetails
from .serializers import RegistrationSerializer
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


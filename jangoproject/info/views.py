from django.shortcuts import render
from rest_framework import generics

from .models import Info
from .serializers import InfoSerializer


class ListInfo(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class DetailInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

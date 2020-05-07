from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Film
from .serializers import FilmSerializer

class FilmAPIView(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

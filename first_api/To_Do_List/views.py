from django.shortcuts import render
from rest_framework import HeroSerializer
from .models import Hero
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset=Hero.objects.all().order_by('name')
    serializer_class=HeroSerializer

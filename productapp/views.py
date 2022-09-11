from rest_framework.response import Response
from rest_framework import (
    generics, 
    permissions, 
    status, 
    )
from rest_framework.views import APIView
from .models import *
from .serializers import *
from datetime import datetime, timedelta
from rest_framework.views import APIView
from django.db.models import CharField, Value, IntegerField, Q
# Create your views here.

class SliderView(generics.ListAPIView):
    serializer_class = SliderSerializer
    permission_classes = ([permissions.AllowAny,])
    authenticated_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Slider.objects.all()

class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = ([permissions.AllowAny,])
    authenticated_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Category.objects.all()

class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = ([permissions.AllowAny,])
    authenticated_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Product.objects.all()   
        query = self.request.GET.get("user_data")
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query)|
                    Q(tag__icontains=query)|
                    Q(type__icontains=query)|
                    Q(category__name__icontains=query)
                    ).distinct()
        return qs   

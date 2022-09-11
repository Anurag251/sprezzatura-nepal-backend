from django.urls import path, include
from .views import *

urlpatterns = [
    path('slider/', SliderView.as_view(), name='slider'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/', ProductView.as_view(), name='product'),
]
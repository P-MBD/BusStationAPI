from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Station, Information
from .serializers import StationSerializer, InformationSerializer

class StationListCreateView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class InformationListCreateView(generics.ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

class StationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    
class StationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Station instances.
    """
    queryset = Station.objects.all()  # تمام ایستگاه‌ها را دریافت می‌کند
    serializer_class = StationSerializer  # از serializer برای تبدیل داده‌ها استفاده می‌کند

class InformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

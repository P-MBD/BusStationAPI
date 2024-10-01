from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StationListCreateView, InformationListCreateView, StationViewSet, StationDetailView, InformationDetailView

urlpatterns = [
    path('stations/', StationListCreateView.as_view(), name='station-list-create'),
    path('stations/<int:pk>/', StationDetailView.as_view(), name='station-detail'),
    path('information/', InformationListCreateView.as_view(), name='information-list-create'),
    path('api/informations/', InformationListCreateView.as_view(), name='information-list-create'),
    path('api/informations/<int:pk>/', InformationDetailView.as_view(), name='information-detail'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockDataViewSet

router = DefaultRouter()
router.register(r'stockdata', StockDataViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]


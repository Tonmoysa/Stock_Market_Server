from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import NotFound  # Add the missing import
from .models import StockData
from .serializers import StockDataSerializer

from rest_framework.pagination import PageNumberPagination

class StockDataPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 100  

       
class StockDataViewSet(viewsets.ModelViewSet):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer
    pagination_class = StockDataPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        trade_code = self.request.query_params.get('trade_code', None)
        date = self.request.query_params.get('date', None)

        if trade_code:
            queryset = queryset.filter(trade_code__iexact=trade_code)  

        if date:  
            queryset = queryset.filter(date=date)
        
        return queryset




       
    
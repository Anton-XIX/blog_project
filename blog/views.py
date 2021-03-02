from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView
)
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .models import Product
from .serializers import *
from rest_framework import filters
from rest_framework.response import Response


class ProductSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class OffsetPagination(LimitOffsetPagination):
    # limit = 5
    limit_query_description = 10
    offset_query_param = '8'


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = OffsetPagination


class NameSearchProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filters.SearchFilter.search_description = 'Type name or part of name '


class ProductNamePatchView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductNameSerializer

    def patch(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)







    # serializer_class = ProductSerializer
    # lookup_field = 'name'
    # queryset = Product.objects.all()
    # def get_queryset(self):
    #     request_name = self.request.query_params.get('name',None)
    #     return Product.objects.filter(name__contains=request_name)

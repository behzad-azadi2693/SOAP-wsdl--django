from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import BookListSerializer, BookDetailSerializer, PublisherSerializer, AuthoreSerializer, CategorySerializer
from .models import BookModel, CategoryModel, AuthoreModel, PublisherModel
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from .soap_service import application
from spyne.server.django import DjangoApplication
# Create your views here.


def soap_book_view(request):
    app = DjangoApplication(application)
    response = app(request)
    return response


class CategoryView(ViewSet):
    serializer_class = CategorySerializer

    def list(self, reqest):
        objs = CategoryModel.objects.all()
        serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data, status=200)


class PublisherView(ViewSet):
    serializer_class = PublisherSerializer

    def list(self, request):
        objs = PublisherModel.objects.all()
        serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data, status=200)


class AuthoreView(ViewSet):
    serializer_class = AuthoreSerializer

    def list(self, request):
        objs = AuthoreModel.objects.all()
        serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data, status=200)


class BookView(ViewSet):

    @extend_schema(responses=BookListSerializer)
    def list(self, request):
        objs = BookModel.objects.all()
        serializer = BookListSerializer(objs, many=True)
        return Response(serializer.data, status=200)
    
    @extend_schema(responses=BookDetailSerializer)
    def retrieve(self, request, pk=None):
        obj = get_object_or_404(BookModel, pk=pk)
        serializer = BookDetailSerializer(obj)
        return Response(obj, status=200)
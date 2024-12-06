from rest_framework import serializers
from .models import CategoryModel, BookModel, PublisherModel, AuthoreModel



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        fields = '__all__'


class AuthoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthoreModel
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['name', 'title', 'thumbnail']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
        depth = 1

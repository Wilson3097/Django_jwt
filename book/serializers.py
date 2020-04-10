from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)

    class Meta:
        model = Book
        fields = ['title', 'amazon_url', 'author', 'genre']

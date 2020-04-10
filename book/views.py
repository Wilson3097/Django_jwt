from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BookListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'

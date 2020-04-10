from django.urls import path, include
from book.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", BookListView)
urlpatterns = [path("book/", include(router.urls))
               ]

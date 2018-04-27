
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('',blog.views.home),
]

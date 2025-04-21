from django.contrib import admin
from django.urls import path, include
from . import views as blog_views
from .views import (PostListView,
                    )

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
]

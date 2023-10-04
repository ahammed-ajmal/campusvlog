from django.urls import path
from . import views
from django.contrib.staticfiles.views import serve

urlpatterns = [
    path('', views.heading_latest, name='heading_latest'),
    path('article/<int:id>', views.single_writing, name='single_writing' ),
]
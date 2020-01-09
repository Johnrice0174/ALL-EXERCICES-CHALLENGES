from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.mainpage, name='home'),
    path('movies_watch/<int:id>', views.watch, name='movies-watch'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    # path('home/<int:number>', views.home, name='home'),
    path('home/<int:number>', views.home, name='home'),
    path('persons/', views.persons, name='person'),
]

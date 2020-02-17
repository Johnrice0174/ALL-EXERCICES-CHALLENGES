from django.shortcuts import render
from django.http import HttpResponse
#from django.urls import reverse
from . import models

def index(request):
    # print((reverse('home')))

    return render(request, "phonebook/index.html")


def home(request, number=0):
    # print("Number = : " + str(number))
    # print(reverse('home', args=[60]))

    return render(request, "phonebook/home.html")


def persons(request):
    person_list = models.Person.objects.all().order_by('last_name')

    person_list_dict = {
        'persons': person_list
    }
    return render(request, "phonebook/person_list.html", person_list_dict)
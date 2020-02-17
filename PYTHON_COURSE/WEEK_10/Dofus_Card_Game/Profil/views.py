from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return 'lol'
    else:
        form = RegisterForm()
    return render(request, 'Profil/register.html', {'formed':form})


def login(request):

    return render(request, 'Profil/login.html')
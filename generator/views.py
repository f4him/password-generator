from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    
    characters = list(string.ascii_lowercase)
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_-=+[]{.},<>?|"))
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))
    
    
    thepassword= ''

    for i in range(length):
        thepassword+=random.choice(characters)


    return render(request, 'generator/password.html', {'password': thepassword})

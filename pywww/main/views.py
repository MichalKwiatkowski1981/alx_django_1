from pprint import pprint
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from main.forms import ContactForm


def hello_world(request: HttpRequest):
    context = {}
    return render(request, 'main/hello.html', context)


def contacts(request: HttpRequest):
    context = {}
    return render(request, 'main/contacts.html', context)


def contact(request: HttpRequest):
    if request.method == 'POST':
        # odbiór danych
        dane_f_formularza = request.POST
        f = ContactForm(request.POST)
        if f.is_valid():
            print('Wyczyszczone dane: ', f.cleaned_data)
        else:
            print('Błędne dane z formularza: ', f.errors)
        return redirect('main:hello_world')
    else:
        context = {'form': ContactForm}
        return render(request, 'main/contact.html', context)




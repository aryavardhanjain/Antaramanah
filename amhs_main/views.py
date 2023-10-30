from django.shortcuts import render



def home(request):
    context = {
        'current_page': 'home',
    }
    return render(request, 'home.html', context)

def our_founders(request):
    context = {
        'current_page': 'founders',
    }
    return render(request, 'founders.html', context)

def mission_vision(request):
    context = {
        'current_page': 'mission_vision',
    }
    return render(request, 'mission_vision.html', context)

def contact(request):
    context = {
        'current_page': 'contact',
    }
    return render(request, 'contact.html', context)

def faq(request):
    context = {
        'current_page': 'faq',
    }
    return render(request, 'faq.html', context)
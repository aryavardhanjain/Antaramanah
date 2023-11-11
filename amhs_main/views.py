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

def services_children(request):
    context = {
        'current_page': 'children',
    }
    return render(request, 'children.html', context)

def services_adolescents(request):
    context = {
        'current_page': 'adolescents',
    }
    return render(request, 'adolescents.html', context)

def services_adults(request):
    context = {
        'current_page': 'adults',
    }
    return render(request, 'adults.html', context)

def services_senior_citizens(request):
    context = {
        'current_page': 'senior_citizens',
    }
    return render(request, 'senior_citizens.html', context)

def services_family(request):
    context = {
        'current_page': 'family',
    }
    return render(request, 'family.html', context)

def services_couples(request):
    context = {
        'current_page': 'couples',
    }
    return render(request, 'couples.html', context)

def services_psychiatric_consultation(request):
    context = {
        'current_page': 'consultation',
    }
    return render(request, 'consultation.html', context)
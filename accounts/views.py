from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages, auth
from therapist.models import Therapist
from django.conf import settings
from .utils import detectUser
from django.contrib.auth.decorators import login_required, user_passes_test

from django.core.exceptions import PermissionDenied

# Create your views here.

# Restrict the therapist from accessing the customer pages.
def check_role_therapist(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied
    
# Restrict the client from accessing the therapist pages.
def check_role_client(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in! ')
        return redirect('myAccount')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, phone_number=phone_number, password=password)
            user.role = User.CLIENT
            user.save()
            messages.success(request,'Your account has been registered successfully. Please click on the activation link on your gmail account.  ')
            return redirect('registerUser')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)

def registerTherapist(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in! ')
        return redirect('myAccount')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, phone_number=phone_number, password=password)
            user.role = User.THERAPIST
            user.save()
            therapist = Therapist()
            therapist.user=user
            user_profile = UserProfile.objects.get(user=user)
            therapist.user_profile = user_profile
            therapist.save()
            messages.success(request, 'Your account has been registered successfully! Please wait for the approval.')
            return redirect ('registerTherapist')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/registerTherapist.html', context)

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in! ')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            if user.get_role() == 'Client':
                auth.login(request, user)

                if remember_me:
                    request.session.set_expiry(60 * 60 * 24 * 21)
                else:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)

                messages.success(request, 'You are now logged in. ')
                return redirect('myAccount')
            else:
                messages.error(request, 'Please login via the therapist login page. ')
                return redirect('login')
        else:
            messages.error(request, 'Invalid login credentials. Please try again. ')
    return render(request, 'accounts/login.html')

def loginTherapist(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in! ')
        return redirect('myAccount')
    elif request.method == 'POST':
        amhs_id = request.POST['amhs_id']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')

        user = auth.authenticate(amhs_id = amhs_id, password = password)

        if user is not None:
            auth.login(request, user)

            if remember_me:
                request.session.set_expiry(60 * 60 * 60 * 21)
            else:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)

            messages.success(request, 'You are now logged in. ')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials. Please try again. ')
            return redirect('loginTherapist')
            
    return render(request, 'accounts/loginTherapist.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'You are now logged out. ')
    return redirect('login')

@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
@user_passes_test(check_role_client)
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
@user_passes_test(check_role_therapist)
def therapistDashboard(request):
    return render(request, 'accounts/therapistDashboard.html')
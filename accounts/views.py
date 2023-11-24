from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages, auth
from therapist.models import Therapist
from django.conf import settings
from .utils import detectUser, send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
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

            #Send verification email
            mail_subject = 'AMHS Account Activation'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)

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

            #Send verification email
            mail_subject = 'AMHS Account Activation'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)

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

def activate(request, uidb64, token):
    #Activate the user by setting the is_active=True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('myAccount')



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

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            #Send reset password email
            mail_subject = 'Reset Your AMHS Password'
            email_template = 'accounts/emails/reset_password_email.html'
            send_verification_email(request, user, mail_subject, email_template) 

            messages.success(request, 'Password reset link has been sent to your email address. ')
            return redirect('forgot_password')
        else:
            messages.error(request, 'Account does not exist. ')
            return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html')

def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Reset your password ')
        return redirect('reset_password')
    else:
        messages.error(request, 'The password reset link has been expired! Please try again. ')
        return redirect('myAccount')

def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset succesful ')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match! Please try again. ')
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')
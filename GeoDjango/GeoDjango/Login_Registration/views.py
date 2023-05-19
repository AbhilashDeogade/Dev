from django.shortcuts import render, redirect
from .forms import SignupForm, PasswordReset, UserProfile, EditAdminForm, CaptchaForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import uuid
from django.core.mail import send_mail
from django.conf import settings


def send_mail_after_registration(email, token):
    subject = "Verify Email"
    message = f'Hi Click on the link to verify your account http://127.0.0.1:8000/auth/account-verify/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home_url')

    form = SignupForm()
    template_name = 'Login&Register/register.html'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            uid = uuid.uuid4()
            profile_obj = Profile(user=new_user,token=uid)
            profile_obj.save()
            send_mail_after_registration(new_user.email, uid)
            messages.success(request, "Your Account Created Successful, to Verify your Account Check Your Email")
            return redirect('signup_url')
    context={'form':form}
    return render(request, template_name, context)


def account_verify(request, token):
    pf = Profile.objects.filter(token=token).first()
    pf.verify = True
    pf.save()
    messages.success(request, "Your account has been verified, you can login")
    return redirect('login_url')



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_url')

    template_name = 'Login&Register/login.html'
    context={}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
    
        user = authenticate(username=un, password=pw)
        
        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect('profile_url')
            messages.success(request, 'you logged in successfully!')
        return redirect('profile_url')           
    return render(request, template_name, context)

def otpLogin(request):
    logout(request)
    template_name = 'Login&Register/login-otp.html'
    context = {}
    return render(request, template_name, context)



def logout_view(request):
    logout(request)
    template_name = 'Login&Register/logout.html'
    context = {}
    return render(request, template_name, context)


def ProfileChangeView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                form = UserProfile(request.POST, instance=request.user)
                users = User.objects.all()
            
            else:
                form = UserProfile(request.POST, instance=request.user)
                users = None
            if form.is_valid():
                messages.success(request, 'Profile Updated successfully!!!')
                form.save()
        else:
            if request.user.is_superuser == True:
                form = EditAdminForm(instance=request.user)
                users = User.objects.all()
            else:
                form = UserProfile(instance=request.user)
                users = None
        return render(request, 'Login&Register/profile.html',  {'name': request.user.username, 'form':form, 'users': users})
    else:
        return redirect('home_url')
   
    
    





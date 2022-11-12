from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from . forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from profile.models import Profile
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # getFormEmail = form.cleaned_data['email']
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            getFormEmail = form.cleaned_data['email']
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            request.user.profile.email = getFormEmail
            request.user.profile.save()
            return redirect('profile:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                request.user.profile.logout_on_all_devices = False
                request.user.profile.save()
                messages.info(request, f"You are now logged in as {email}")
                return redirect('/')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})


def logout_view(request):
    logout(request)
    return redirect('profile:home')


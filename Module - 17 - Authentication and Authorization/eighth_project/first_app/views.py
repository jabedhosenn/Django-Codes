from django.shortcuts import render, redirect
from requests import request
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash


# Create your views here.
def home(request):
    return render(request, "./home.html")


# def signup(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 messages.success(request, "Account created successfully.")
#                 form.save()
#         else:
#             form = RegisterForm()
#         return render(request, "./home.html", {"form": form})
#     else:
#         return redirect("profile")


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account created successfully")
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, "./signup.html", {"form": form})
    else:
        return redirect("profile")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    # return render(request, './home.html')
                    return redirect("profile")
                else:
                    messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()
        return render(request, "./login.html", {"form": form})
    else:
        return redirect("profile")


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, "Account updated successfully")
                form.save()
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, "./profile.html", {"form": form})
    else:
        return redirect("signup")


def user_logout(request):
    logout(request)
    return redirect("login")


# def pass_change(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PasswordChangeForm(request.user, request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 update_session_auth_hash(request, user)
#                 messages.success(request, 'Your password was successfully updated!')
#                 return redirect('profile')
#             else:
#                 messages.error(request, 'Please correct the error below.')
#     else:
#         return redirect('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "./passchange.html", {"form": form})
    else:
        return redirect("login")


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, "./passchange.html", {"form": form})
    else:
        return redirect("login")


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, "Account updated successfully")
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(request, "./profile.html", {"form": form})
    else:
        return redirect("signup")

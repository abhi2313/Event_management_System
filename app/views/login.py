
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginuser, logout
from django.contrib import messages


class Login(View):
    valuenext = None

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        message = None
        form = AuthenticationForm()
        context = {
            'form': form,
            'message': message
        }
        return render(request, 'login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        valuenext = request.GET.get('next')

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginuser(request, user)
                if valuenext is None:
                    return redirect('homepage')
                else:
                    return redirect(valuenext)
            else:
                message = "User Not exist."
                return render(request, 'login.html', context={'form': form, 'message': message})
        else:
            expalnation = form.errors.as_data()
            for key in expalnation:
                for value in expalnation[key]:
                    message = value
            context = {
                'form': form,
                'message': message
            }

            return render(request, 'login.html', context)

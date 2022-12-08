
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,login as loginuser
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from app.forms import UserRegistrationForm

from django.contrib import messages

class Signup(View):
    message=None
    def get(self, request):
        form = UserRegistrationForm()
        message=None
        context = {'form': form,'message':message}
        return render(request, 'signup.html', context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None:
                loginuser(request,user)
                return redirect('homepage')

           
        else:
            expalnation=form.errors.as_data()
            for key in expalnation:
                for value in expalnation[key]:
                    message=value
            form = UserRegistrationForm()
            context = {'form': form,'message':message}
            return render(request, 'signup.html', context)

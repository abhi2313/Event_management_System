
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,login as loginuser
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from app.forms import UserRegistrationForm


class Signup(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'signup.html', context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None:
                loginuser(request,user)
                return redirect('homepage')

            # messages.success(request, f'Your account has been created. You can log in now!')
            # return redirect('login')
        else:
            form = UserRegistrationForm()
            context = {'form': form}
            return render(request, 'signup.html', context)

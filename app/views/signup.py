
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from app.forms import UserRegistrationForm



class Signup(View):
    def get(self,request):
        form=UserRegistrationForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    def post(self,request):
        form = UserRegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user=form.save()
            if user is not None:
                return redirect('homepage')
            

            # messages.success(request, f'Your account has been created. You can log in now!')    
            # return redirect('login')
        else:
            form = UserRegistrationForm()
            context = {'form': form}
            return render(request, 'signup.html', context)
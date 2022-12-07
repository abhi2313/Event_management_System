from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from app.forms import eventForm
from app.models import invites


@login_required(login_url='login')
def add_an_event(request):
    user = request.user
    form = eventForm(request.POST)
    if form.is_valid():
        
        event = form.save(commit=False)
        event.host = user
        event.datetime=datetime.datetime.now()
        event.save()
        invite=invites(user=user,event=event)
        invite.save()

        # print(event.invited)
        return redirect('add_event')
    else:
        return render(request, 'add_an_event.html', context={'form': form})

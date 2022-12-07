from django.shortcuts import render,redirect
from app.models import events
def you_invited(request):
    user=request.user
    obj=events.objects.filter(invited_user=user)
    context={
        'objs':obj
    }
    print(obj)
    return render(request,'see_events_you_invited.html',context)
    
    

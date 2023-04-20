from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Szakdoga
from .forms import Szakdogaform
# Create your views here.


def index(request):
    form = Szakdogaform(request.POST or None)
    if(request.method == "POST"):
        if(form.is_valid()):
            form.save()
            form = Szakdogaform()
    else:
        form = Szakdogaform()

    szakdolgozatok = Szakdoga.objects.all()
    context = {
        'form' : form,
        'szakdolgozatok' : szakdolgozatok
    }


    return render(request, "app/index.html", context= context)


def szakdogaModosit(request, id):
    szakdoga = get_object_or_404(Szakdoga, pk = id)
    form = Szakdogaform(request.POST or None, instance= szakdoga)
    if(request.method == 'POST'):
        if(form.is_valid):
            form.save()
            return redirect(index)
        
    context = {
        'form' : form

    }
    return render(request, "app/modositas.html", context= context)


def szakdogaTorles(request, id):
    szakdoga = get_object_or_404(Szakdoga, pk = id)
    szakdoga.delete()
    return redirect(index)
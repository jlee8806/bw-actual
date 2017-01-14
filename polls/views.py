from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from .forms import rsvp_form
from .models import rsvp
from django.contrib import messages
from django.http import Http404

def index(request):

    return render(request, 'polls/index.html')
def wp(request):

    return render(request, 'polls/weddingparty.html')
def travel(request):

    return render(request, 'polls/travel.html')
def gallery(request):

    return render(request, 'polls/gallery.html')

def rsvp_page(request):
    form = rsvp_form(request.POST)
    if request.method == 'POST':
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Thank You!")
            return redirect('index')
    context={
        'form' : form
    }
    return render(request, 'polls/rsvp.html', context)

def info(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('index')
    queryset_list = rsvp.objects.all().order_by('name')
    context = {
        'object_list': queryset_list,

    }
    return render(request, 'polls/info.html', context)

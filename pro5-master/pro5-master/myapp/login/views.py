# Create your views here.
#views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

from .forms import *
from models import *


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )


def register_success(request):
    return render_to_response(
    'registration/success.html',
    )


def about(request):
    return render_to_response('registration/about.html',)
def blog(request):
    return render_to_response('registration/blog.html',)
def contact(request):
    return render_to_response('registration/contact.html',)
def details_ITCOcean(request):
    return render_to_response('registration/details_ITCOcean.html',)
def details(request):
    return render_to_response('registration/details.html',)
def details_cgin(request):
    return render_to_response('registration/details_cgin.html',)
def details_coral(request):
    return render_to_response('registration/details_coral.html',)
def details_fish(request):
    return render_to_response('registration/details_fish.html',)
def details_forecast(request):
    return render_to_response('registration/details_forecast.html',)
def details_sat(request):
    return render_to_response('registration/details_sat.html',)
def details_storm(request):
    return render_to_response('registration/details_storm.html',)
def details_storm2(request):
    return render_to_response('registration/details_storm2.html',)
def details_warn(request):
    return render_to_response('registration/details_warn.html',)
def service(request):
    return render_to_response('registration/service.html',)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )



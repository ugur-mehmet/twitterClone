from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from models import Kullanici, Twit, Takip, DM
from forms import SignupForm
from django.contrib import auth

# Create your views here.\
@login_required
def index(request):
	cookie = request.COOKIES.get('remind_me')
	kullanici_id = request.session['kullanici_id']
	takip_eden_listesi = Takip.objects.filter(eden__id=kullanici_id)
	takip_edilen_listesi = Takip.objects.filter(edilen__id=kullanici_id)
	takip_edilen_sayi = takip_edilen_listesi.count()
	takip_eden_sayi = takip_eden_listesi.count()
	c = {'edilen_sayi':takip_edilen_sayi, 'eden_sayi':takip_eden_sayi, 
		'eden_liste':takip_eden_listesi, 'edilen_liste':takip_edilen_listesi}
	return render_to_response("index.html",c)

def login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'],password=request.POST['password']) 
		if user is not None:
			auth.login(request, user)
			request.session['kullanici_id'] = user.id
			response = redirect('/twitter/index')
			response.set_cookie('remind_me',True)
			return response		
	c = {}
	c.update(csrf(request))
	return render_to_response("login.html",c)

@login_required
def logout(request):
	auth.logout(request)
	return redirect('/twitter/index')

def signup(request):
	c = {}
	c.update(csrf(request))
	if request.method != "POST":
		form = SignupForm()
	else:
		form = SignupForm(request.POST)
		if form.is_valid():
			u = User.objects.create_user(email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'),
						username=form.cleaned_data.get('email'))
			u.save()
			return redirect('/twitter/index')
	c['form'] = form
	return render_to_response('signup.html',c)

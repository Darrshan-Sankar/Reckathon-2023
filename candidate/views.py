import io
import os
import json
from bardapi import Bard
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import  JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm

os.environ['_BARD_API_KEY']="YwgymR5cBCjS_MuUWUQ85qcW5FyjJBd3-AFHS41iXfqPO3glSe4ULM89sHlVUrO2eLa_KA."
bd = Bard()

# Create your views here.
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        resp = bd.get_answer(data['message'])['content']
        response = {'message': resp, 'csrf_token': get_token(request)}
        return JsonResponse(response)

def candidate_form(request):
    return render(request, 'main.html')
def form(request):
    return render(request, 'form.html')

def idea(request):
    from django.shortcuts import render, redirect
from .forms import IdeaForm

def idea_submit(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('idea_submit_success')  # Replace 'idea_submit_success' with the URL name of the success page
    else:
        form = IdeaForm()

    return render(request, 'idea.html', {'form': form})

def idea_submit_success(request):
    return render(request, 'idea_submit_success.html')

# Your other views go here...


# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

def login_signup(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main')  # Replace 'home' with the URL name of your home page
                else:
                    messages.info(request, 'Invalid Username or Password.')
            else:
                signup_form = SignupForm()
        elif 'signup' in request.POST:
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                # You can access other form fields in a similar way

                # Example implementation:
                user = User.objects.create_user(email=email, password=password)
                user.save()

                login(request, user)
                return redirect('main')  # Replace 'home' with the URL name of your home page
            else:
                login_form = LoginForm()
    else:
        login_form = LoginForm()
        signup_form = SignupForm()

    return render(request, 'form.html', {'login_form': login_form, 'signup_form': signup_form})
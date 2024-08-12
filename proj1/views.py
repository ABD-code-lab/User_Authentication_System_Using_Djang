from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    data = {}
    if request.method == 'POST':
        username12 = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        data = {
            'user':username12,
        }
        
        # if username12 == '':
        #     return HttpResponse('Invalid')
        
        x = User.objects.create_user(username=username12, first_name=first_name, last_name=last_name, email=email, password=password)
        x.save()
    
    return render(request, 'signup.html', data)

def signin(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        
        x = auth.authenticate(username=username, password=password)
        if x is None:
            return render(req, 'error.html')
        else:
            return render(req, 'main.html')
            
    return render(req, 'signin.html')

def error(req):
    return render(req, 'error.html')

def main(req):
    return render(req, 'main.html')
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    # return HttpResponse("HELLO")
    if request.method == "POST":
        # username = request.POST.get('username')
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        # gender = request.POST['inlineRadioOptions']
        email = request.POST['email']
        firstname = request.POST['firstname']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        # myuser = User.objects.create(username, email, password)
        myuser = User.objects.create_user(username=username, email=email, password=password)

        myuser.first_name = firstname
        myuser.last_name = lastname
        
        myuser.save()
        
        messages.success(request, "your Account has been successfully created!!")
        
        return redirect("signin")
        
        
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            fname =  user.first_name
            return render(request, "authentication/index.html", {'fname':fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
        
        
    return render(request, "authentication/signin.html")


def signout(request):
    pass
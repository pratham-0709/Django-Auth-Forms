from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def Login(request):
    return render(request, 'login.html')

def Register(request):
    if request.method == "POST":
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(uname = uname).exists():
                message.error("Username Exists")
            if User.objects.filter(email = email).exists():
                message.error("Email Exists")
            else:
                user = User.objects.create(username = username, first_name = fname, last_name = lname, email = email, password = pass1)
                user.save()
                if user is not None:
                    auth.login(request, user)
                    return HttpResponse("Registration Success")

        else:
            messages.error(request, "Both Password are not Matching")

    return render(request, 'login.html')

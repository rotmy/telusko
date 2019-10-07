from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Register(request):

    if request.method == 'POST':                     # This is a POST method to post the collected Data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # (model)=(input)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('Register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('Register')
        return redirect('/')  # To return to the homepage

    # To call GET function for the login form
    return render(request, 'Register.html')


def logout(request):
    auth.logout(request)
    return redirect("/")

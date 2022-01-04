
from django.shortcuts import redirect,render
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
      return render(request, "authSystem/index.html")


def signup(request):

    if request.method == "POST":
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        city=request.POST['city']
        rfl=request.POST['rfl']
        password1=request.POST['password1']
        password2=request.POST['password2']

        myuser=User.objects.create_user(email,password1)
        myuser.full_name=name

        myuser.save()

        messages.success(request,"your account is successfully created.")
        return redirect('signin')
    
    return  render(request, "authSystem/signup.html") 

        



def signin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']

        user = authenticate(email=email,password=password1)
        

        if user is not None:
            login(request, user)
            name=user.name
            email=user.email
            return render(request, "authSystem/index.html",{'name':name})

        else:
            messages.error(request, "Wrong credentials!")
            return redirect('home')    

    return render(request, "authSystem/signin.html")   



def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')  


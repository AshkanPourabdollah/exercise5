from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,"products/index.html")

def contact(request):
    return render(request,"products/contact.html")

def users(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        users = authenticate(request,username = name , password = password)
        if users is not None : 
            login(request,users)
            return redirect("/userPanel")
        else:
            return HttpResponse("error")
    return render(request,"products/users.html")



from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "POST":
        name = request.POST.get("register_name")
        lastName = request.POST.get("register_last_name")
        email = request.POST.get("register_email")
        password = request.POST.get("register_password")
        confirmPassword = request.POST.get("register_confirm_password")

        User.objects.create_user(username=name, password=password, email=email)

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)

        return redirect("/userPanel")

    return render(request,"products/register.html")

def products(request):
    return render(request,"products/products.html")



def user_panel(request):
    if request.user.is_authenticated:
        return render(request,"products/user_index.html")
    else:
        return redirect("/")

def user_logout(request):
    logout(request)
    return redirect("/")

def user_products(request):
    return render(request,"products/user_products.html")

def user_contact_us(request):
    return render(request,"products/user_contact_us.html")
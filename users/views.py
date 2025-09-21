from django.shortcuts import render,redirect
from .form import RegisterForm
from django.contrib.auth import logout,login

from.form import UserLoginForm
# Create your views here.



from django.contrib import messages

def register(request):
    form=RegisterForm(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True   
            user.save()
            messages.success  (request, "Account created successfully! You can now log in.")
            return redirect("users:login")

        
    print(form.errors)
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Role-based redirect
            if user.role == "admin":
                return redirect("complaint:admin_dashboard")
            else:
                return redirect("complaint:user_dashboard")
    else:
        form = UserLoginForm()


    return render(request, "users/login.html", {"form": form})  

def logout_view(request):
    logout(request)


    return render(request,"users/logout.html")
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authticase
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in successfully")
            return redirect("home")
        else:
            messages.warning(request, "There was an error, please try again later")
            return redirect("home")
    else:
        return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "User logged out successfully.")
    return redirect("home")

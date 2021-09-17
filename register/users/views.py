
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "students/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'students/index.html', {
            "students": Student.objects.get(username = username)
        })

        else:
            return render(request, "users/login.html",{
                "message": "Invalid credentials"
            })
    return render(request, "users/login.html")



def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
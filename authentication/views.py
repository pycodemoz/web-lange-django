from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
          login(request, form.get_user())
          return redirect('parents')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

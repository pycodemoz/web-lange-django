from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


@login_required(login_url='login')
@permission_required('users.add_user', raise_exception=True)
def registration_view(request):
  if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
        login(request,form.save())
        return redirect('login')
  else:
      form = UserCreationForm()
  return render (request, 'registration.html', {"form": form})

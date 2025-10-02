from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ParentForm
from .models import Parent


@login_required(login_url='login')
def parents_view(request):
  parents = Parent.objects.all()
  nav_parents = Parent.objects.all()[:4]
  context = {'parents': parents,
             'nav_parents': nav_parents,
             
  }
  return render(request, 'parents.html', context)

@login_required(login_url='login')
def parent_create(request):
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parents')  
    else:
        form = ParentForm()
    return render(request, 'parent_create.html', {'form': form})


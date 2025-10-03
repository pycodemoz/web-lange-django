from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ParentForm
from .models import Parent


@login_required(login_url='login')
def parents_view(request):  
    parents = Parent.objects.all()
    nav_parents = Parent.objects.all()[:4]
    context = {
        'parents': parents,
        'nav_parents': nav_parents,
    }
    return render(request, 'parents.html', context)


@login_required(login_url='login')
@permission_required('parents.add_parent', raise_exception=True)
def parent_create(request):
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parents')  
    else:
        form = ParentForm()
    return render(request, 'parent_create.html', {'form': form})


@login_required(login_url='login')
@permission_required('parents.change_parent', raise_exception=True)
def parent_update(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('parents')
    else:
        form = ParentForm(instance=parent)
    
    context = {
        'form': form,
        'parent': parent
    }
    return render(request, 'parent_update.html', context)


@login_required(login_url='login')
@permission_required('parents.delete_parent', raise_exception=True)
def parent_delete(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    
    if request.method == 'POST':
        parent.delete()
        return redirect('parents')
    
    context = {'parent': parent}
    return render(request, 'parent_delete.html', context)


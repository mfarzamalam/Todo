from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.
def action(request):
    return render(request, 'crud/action.html')

def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:read')
    else:
        form = UserForm

    context = {'form':form}
    return render(request, 'crud/create.html', context)


def read(request):
    users = User.objects.all()

    context = {'users':users}
    return render(request, 'crud/read.html', context)


def update(request,pk):
    user = User.objects.get(pk=pk)
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('crud:read')

         
    context = {'form':form}
    return render(request, 'crud/update.html', context)

def delete(request,pk):
    user = User.objects.filter(pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('crud:read')

    else:
        return render(request, 'crud/delete.html')

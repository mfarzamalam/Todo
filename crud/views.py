from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.
def create_read(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/action')
    else:
        form = UserForm

    users = User.objects.all()
    context = {'form':form, 'users':users}
    return render(request, 'crud/action.html', context)


def update(request,pk):
    user = User.objects.get(pk=pk)
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/action')

    users = User.objects.all()
    context = {'form':form, 'users':users}
    return render(request, 'crud/action.html', context)

def delete(request,pk):
    user = User.objects.filter(pk=pk)
    user.delete()

    return redirect('/action')

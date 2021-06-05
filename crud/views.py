from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.http import JsonResponse

# Create your views here.
def read(request):
    form = UserForm
    users = User.objects.all()

    context = {'form':form, 'users':users}
    return render(request, 'crud/action.html', context)


def create(request):
     if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            users = User.objects.values()
            # print(users)
            users_data = list(users)
            # print(user_data)
            return JsonResponse({'status':"Saved", 'users_data':users_data})

        else:
            return JsonResponse({'status':0})


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

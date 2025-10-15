from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def get_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'all_users.html', context)

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('all_users')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form, 'title': 'Create User'})

def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully')
            return redirect('all_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form, 'title': 'Update User'})

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, 'User deleted successfully')
    return redirect('all_users')

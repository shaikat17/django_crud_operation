from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistration
from .models import User

# Create your views here.

# Add new User and Show all User
def add_show(request):
    if request.method == 'POST':
        userForm = UserRegistration(request.POST)
        if userForm.is_valid():
            userForm.save()
            userForm = UserRegistration()
    else:
        userForm = UserRegistration()
    all_user = User.objects.all().order_by('-id')
    return render(request, 'crud/addshow.html', {'form' : userForm, 'all_user': all_user})

# This Function will update/edit
def update_user(request, id):
    if request.method == 'POST':
        user_data = User.objects.get(pk=id)
        user_form = UserRegistration(request.POST, instance=user_data)
        if user_form.is_valid():
            user_form.save()
    else:
        user_data = User.objects.get(pk=id)
        user_form = UserRegistration(instance=user_data)
    return render(request, 'crud/update.html', {'form' : user_form})

# Delete User
def delete_user(request, id):
    if request.method == 'POST':
        dlt_data = User.objects.get(pk=id)
        dlt_data.delete()
        return HttpResponseRedirect('/')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_view(request):
    if request.method == "POST":
        user_register = UserCreationForm(request.POST)
        if user_register.is_valid():
            user_register.save()
            return redirect('login')
    else:
        user_register = UserCreationForm()
    return render(
        request,
        'register.html',
        {'user_register': user_register}
    )

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(
        request
        , 'login.html',
        {'login_form': login_form}
    )


def logout_view(request):
    logout(request)
    return redirect('cars_list')


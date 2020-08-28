from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm

# Create your views here.
from django.urls import reverse_lazy
from .models import Order


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        form = RegisterForm
        return render(request, 'signup.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


def login_form(request):
    if request.method == 'GET':
        form = LoginForm
        return render(request, 'login_form.html', {'forms': form})

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                print(request.GET)
                if 'next' in request.GET.keys():
                    messages.success(request, ' login success')
                    return redirect(request.GET['next'])
                else:
                    return redirect('index')

            else:
                return redirect('login')
        else:

            messages.error(request, 'invalid username or password')
            return redirect('login')


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url=reverse_lazy('login'))
def order(request):
    if request.method == 'GET':
        return render(request, 'order.html')

    elif request.method == 'POST':
        # username = request.POST['username']
        # user = authenticate(username=username)
        # print(username)
        # print(user)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        Order.objects.create(
            username=request.POST['username'],
            qty=request.POST['qty'],
            choose_cylinder=request.POST['cylinder'],
            time=request.POST['Time'],
            path_name=request.POST['sname'])
        return redirect('index')


def about_us(request):
    return render(request, 'aboutus.html')

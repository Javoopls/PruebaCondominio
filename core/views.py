from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.decorators import residente_only

# Create your views here.

def carrito(request):
    context = {}
    return render(request, 'core/carrito.html', context)

def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def pago(request):
    context = {}
    return render(request, 'core/pago.html', context)

def login_success(request):
    if request.user.groups.filter(name="admin").exists():
        return redirect('/admin/')
    else:
        return redirect('user')

@login_required(login_url='login')
@residente_only
def user(request):
    return render(request, 'core/user.html')

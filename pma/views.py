from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signin(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        pwd=request.POST.get('pwd')
        user=authenticate(request,username=un,password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
    return render(request,'login.html')
def dashboard(request):
    return render(request,'dashboard.html')
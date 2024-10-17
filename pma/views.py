from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
# Create your views here.
a='hello'
def signin(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        pwd=request.POST.get('pwd')
        user=authenticate(request,username=un,password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request,'login.html')
@login_required(login_url='/login')
def signout(request):
    logout(request)
    return redirect('/login')
@login_required(login_url='/login')
def dashboard(request):
    return render(request,'manager/dashboard.html',{'a':a})
@login_required(login_url='/login')
def caseslists(request):
    cl=Cases.objects.filter(is_active=True)
    print(cl)
    return render(request,'manager/caseslist.html',{'cl':cl})
@login_required(login_url='/login')
def fiblists(request):
    fibl=FIbranch.objects.filter(is_active=True)
    print(fibl)
    return render(request,'manager/fibranchlists.html',{'fibl':fibl})
@login_required(login_url='/login')
def createfibranch(request):
    if request.method == 'POST':
        finame = request.POST.get('finame')
        location = request.POST.get('location')
        print(finame,location)
        FIbranch.objects.create(finame=finame,location=location)
        messages.success(request, f'FIBranch {finame} Created Successfully!')
        return redirect('/fiblists')
    return render(request,'manager/createfibranch.html')
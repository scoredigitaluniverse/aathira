from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count,F
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
        else:
            messages.success(request, f'Invalid Username!')
    return render(request,'login.html')
@login_required(login_url='/login')
def signout(request):
    logout(request)
    return redirect('/login')
@login_required(login_url='/login')
def dashboard(request):
    total_cases = Cases.objects.count()
    fi_cases_count = FIbranch.objects.annotate(
        num_cases=Count('cases'),
        percentage=F('num_cases') * 100 / total_cases  # Calculate percentage
    )
    return render(request,'manager/dashboard.html',{'a':a,'fi_cases_count':fi_cases_count,'total_cases': total_cases})
@login_required(login_url='/login')
def caseslists(request):
    cl=Cases.objects.filter(is_active=True)
    print(cl)
    return render(request,'manager/caseslists.html',{'cl':cl})
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
@login_required(login_url='/login')
def createcases(request):
    fibl=FIbranch.objects.filter(is_active=True)
    if request.method == "POST":
        caseid = request.POST.get('caseid')
        applicantname = request.POST.get('applicantname')
        mobilenumber =request.POST.get('mobilenumber')
        finame_id=request.POST.get('finame')
        finame=FIbranch.objects.get(id=finame_id)
        Cases.objects.create(caseid=caseid,applicantname=applicantname,finame=finame,applicant_mobile_number=mobilenumber)
        messages.success(request, f'Case {caseid} Created Successfully!')
        return redirect('/caseslists')
    return render(request,'manager/createcases.html',{'fibl':fibl})
@login_required(login_url='/login')
def deletecases(request,id):
    obj = get_object_or_404(Cases, id=id)
    obj.delete()
    return redirect('/caseslists')
@login_required(login_url='/login')
def updatecases(request,id):
    fibl=FIbranch.objects.filter(is_active=True)
    obj = get_object_or_404(Cases,id=id)
    if request.method == 'POST':
        obj.caseid = request.POST.get('caseid')
        obj.applicantname =request.POST.get('applicantname')
        obj.applicant_mobile_number=request.POST.get('mobilenumber')
        finame_id=request.POST.get('finame')
        finame=FIbranch.objects.get(id=finame_id)
        obj.finame = finame
        obj.save()
        messages.success(request, f'Case {obj.caseid} Updated Successfully!')
        return redirect('/caseslists')
    return render(request,'manager/updatecases.html',{'obj':obj,'fibl':fibl})
@login_required(login_url='/login')
def deletefibranch(request,id):
    obj = get_object_or_404(FIbranch, id=id)
    finame=FIbranch.objects.get(id=id)
    obj.delete()
    messages.error(request, f'FIbranch {finame.finame} deleted Successfully!')
    return redirect('/fiblists')
@login_required(login_url='/login')
def updatefibranch(request,id):
    obj = get_object_or_404(FIbranch, id=id)
    if request.method == "POST":
        obj.finame = request.POST.get('finame')
        obj.location = request.POST.get('location')
        obj.save()
        messages.success(request, f'Case {obj.finame} Updated Successfully!')
        return redirect('/fiblists')
    return render(request,'manager/updatefiblists.html',{'obj':obj})
@login_required(login_url='/login')
def employeeslists(request):
    u=User.objects.filter(is_superuser=False)
    return render(request,'manager/employeeslists.html',{'u':u})
@login_required(login_url='/login')
def createemployees(request):
    if request.method == "POST":
        un = request.POST.get('empname')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        if User.objects.filter(username=un).exists():
            messages.success(request, 'Username already exists')
            return render(request, 'manager/createemployees.html')
        if User.objects.filter(email=email).exists():
            messages.success(request, 'Email already exists')
            return render(request, 'manager/createemployees.html')
        user=User.objects.create_user(username=un,email=email,password=pwd)
        user.save()
        messages.success(request, f'New User {un} Created Successfully!')
        return redirect('/employeeslists')
    return render(request,'manager/createemployees.html')
@login_required(login_url='/login')
def deleteemployee(request,id):
    obj = get_object_or_404(User, id=id)
    user=User.objects.get(id=id)
    obj.delete()
    messages.error(request, f'User {user.username} deleted Successfully!')
    return redirect('/employeeslists')
def activeemployee(request,id):
    obj = get_object_or_404(User, id=id)
    user=User.objects.get(id=id)
    if obj.is_active:
        obj.is_active = False
        messages.error(request, f'User {user.username} Inactivated Successfully!')
    else:
        obj.is_active = True
        messages.error(request, f'User {user.username} activated Successfully!')
    obj.save()
    return redirect('/employeeslists')
@login_required(login_url='/login')
def updateemployee(request,id):
    obj = get_object_or_404(User, id=id)
    if request.method == "POST":
        obj.username = request.POST.get('empname')
        obj.email = request.POST.get('email')
        obj.save()
        messages.success(request, f'User {obj.username} Updated Successfully!')
        return redirect('/employeeslists')
    return render(request,'manager/updateemployee.html',{'obj':obj})
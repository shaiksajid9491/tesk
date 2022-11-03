from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import EmployeeForm
from .models import Employee


# Create your views here.


def home(request):
    return HttpResponse("<h1> my home</h1>")


def town(request):
    return HttpResponse("<h1>home town</h1>")


def table(request):
    emp = Employee.objects.all()
    return render(request, "table.html", {"record": emp})


def user_table(request):
    user = User.objects.all().values("username", "password", "first_name", "last_name",'email_address')
    print(user)
    return render(request, "user.html", {"data": user})

def create(request):
    if request.method=='POST':
        print(request.POST)
        form=EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/table/')
    else:
            form=EmployeeForm()
    return render(request,'create.html',{'form':form})

def edit(request,id):
    emp_data = Employee.objects.get(id=id)
    form=EmployeeForm(instance=emp_data)
    return render(request, "update.html", {'form': form, 'id': id})




def update(request,id):
    emp_data = Employee.objects.get(id=id)
    form= EmployeeForm(request.POST, instance=emp_data)
    if form.is_valid():
        form.save()
        return redirect('/table/')
    return render(request, "update.html", {'form': form,'id': id})



def delete(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/table/')

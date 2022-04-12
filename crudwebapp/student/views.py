from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import studentRegistration
from .models import User
# Create your views here.
#this function is for adding the new items
def add_show(request):
    if request.method=="POST":
        fm=studentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            reg=User(name=name,email=email,password=password)
            reg.save()
            fm=studentRegistration()
    else:
        fm=studentRegistration()
    stud=User.objects.all()
    return render(request,'student/addshow.html',{'form':fm,'stu':stud})
#function for deleting the row
def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
#thi function will update/edit
def update(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=studentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi=User.objects.get(pk=id)
            fm=studentRegistration(instance=pi)
    return render(request,'student/updatestudent.html',{'form':fm})
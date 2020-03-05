from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def Registration(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form=UserCreationForm()
    context={
    'form':form
    }
    return render(request,'accounts/registration.html',context)
@login_required
def ProfileUpdateView(request):
    user_obj=UserProfile.objects.get(user=request.user)
    if request.method=="POST":
        form=ProfileUpdateForm(request.POST or None,request.FILES or None,instance=user_obj)
        u_form=UserUpdateForm(request.POST or None,instance=request.user)
        if form.is_valid and u_form.is_valid:
            form.save()
            u_form.save()
            u_form=UserUpdateForm()
            form=ProfileUpdateForm()
    else:
        u_form=UserUpdateForm()
        form=ProfileUpdateForm()
    context={
    'form':form,
    'obj':user_obj,
    'u_form':u_form
    }
    return render(request,'accounts/profile.html',context)

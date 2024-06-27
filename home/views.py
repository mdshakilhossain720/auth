from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .forms import SignUp
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        fm=SignUp(request.POST)
        if fm.is_valid():
            fm.save()
    else:
     fm=SignUp()
    return render(request,'signup.html',{'form':fm})


# login view 

def userlogin(request):
   if request.method == 'POST':
      fm=AuthenticationForm(request=request,data=request.POST)
      if fm.is_valid():
         nm=fm.cleaned_data['username']
         pw=fm.cleaned_data['password']
         user=AuthenticationForm(username=nm,password=pw)
         if user is not None:
            login(request,user)
            return HttpResponseRedirect('/profile/')
    


   else:
   
     fm=AuthenticationForm()

   return render(request,'userlogin.html',{'from':fm})


# profile view

def profileview(request):
   return render(request,'profile.html')


# logout page 
def logoutpage(request):
   logout(request)
   return HttpResponseRedirect('/login/')

# change pass
def changepass(request):
   if request.user.is_authenticated:
      if request.method == 'POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
         fm.save()
         update_session_auth_hash(request,fm.user)
         return HttpResponseRedirect('/profile/')
      else:
      
       fm=PasswordChangeForm(user=request.user)
      return render(request,'change.html',{'from':fm})
   else:
      return HttpResponseRedirect('/profile/')


   


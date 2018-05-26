from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .forms import LoginForm
from .forms import regForm
from .models import LoginApp

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello Login</h1>')



def Login_form(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request,'Login_form.html',{'form':form})


def Login_success(request):
    context = {'success':'successfully'}
    return render(request,'success_post.html',context)


def register(request):
    Reg_form = regForm(request.POST)
    if Reg_form.is_valid():
        instance = Reg_form.save(commit=False)
        instance.save()
        return HttpResponseRedirect()

    context={'reg_form':Reg_form}
    return render(request,'reg_form.html',context)

from django.shortcuts import *
from .import views
from .models import *

# Create your views here.


def homepage(request):
    return render(request,"app/home.html")


def datapage(request):
    user1=request.POST['username']
    pass1=request.POST['password']
    email1=request.POST['Email']

    newuser=user.objects.create(uname=user1,passw=pass1,email=email1)
    return HttpResponseRedirect(reverse('display'))

def showdata(request):
    all=user.objects.all()
    return render(request,"app/data.html",{'key1':all})

def edit(request):
        e = request.POST['e']
        one_user = user.objects.filter(id=e)
        return render(request,"app/edit.html",{'key':one_user})



def change(request):
        u=request.POST['username']
        e=request.POST['email']
        p=request.POST['password']
        ide=request.POST['i']

        newuser=user.objects.get(id=ide)

        if u=="":
                pass
        else:
                newuser.uname = u
                newuser.save()
        if e=="":
                pass
        else:
                newuser.email = e 
                newuser.save()
        
        if p=="":
                pass

        else:   
                newuser.passw = p
                newuser.save()

        alluser=user.objects.all()
        return render(request,"app/data.html",{'key1':alluser})



def delete(request):
        e = request.POST['d']
        one_user = user.objects.filter(id=e)
        one_user.delete()
        alluser=user.objects.all()
        return render(request,"app/data.html",{'key1':alluser})



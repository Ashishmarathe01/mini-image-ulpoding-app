from django.shortcuts import render,redirect,HttpResponseRedirect
from random import randint

from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
import re
from .models import Blog
from django.conf import settings
from django.contrib import messages
# Create your views here.


def singUp(request):
    # this for making random number
    x = randint(1, 10)
    y = randint(1, 10)
    m=[]
    l=x+y
    m.append(l)
    x1 = []
    y1 = []
    x1.append(x)
    y1.append(y)
    z = x1 + y1
    data = {'x':x,'y':y,'l':l}

    if request.method == 'GET':
        return render(request, "Mpost/singUp.html", data)

    if request.method =='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('fname')
        password = request.POST.get('password')
        password2=request.POST.get('password2')
        o = request.POST.get('r1',default=0)
        b=int(o)
        print(type(b))

        num1=request.POST.get('num1')
        p=int(num1)

        print(b)
        print(num1)

        if p == b:
            print("true")
            if password == password2:
                print('true')
                f1 = 0
                while True: # this is for cheking alphanumeric value

                    if (len(password) < 8):
                        print("t1")
                        f1 = -1
                        break
                    elif not re.search('[a-z]', password):
                        print("t2")
                        f1 = -1
                        break
                    elif not re.search('[A-Z]', password):
                        print("t3")
                        f1 = -1
                        break
                    elif not re.search('[0-9]', password):
                        print("t4")
                        f1 = -1
                        break
                    elif not re.search('[_@$]', password):
                        print("t5")
                        f1 = -1
                        break
                    elif re.search("\s", password):
                        print("t6")
                        f1 = -1
                        break
                    else:
                        print("t7")
                        f1 = 0
                        if User.objects.filter(username=username).exists():
                            messages.info(request, 'User name Exit!!')
                            return redirect("singup")

                        else:
                            user = User.objects.create_user(username=username, first_name=first_name,
                                                            password=password)
                            user.save()
                            messages.info(request, 'you are Login!!')
                            return redirect("login")
                            print("evrythiong ok")
                        print("this is valid ")

                        break

                if f1 == -1:
                    print("t8")
                    print("not valid")
                    messages.info(request,  'Check password it should be more than 8 character and Alphanumeric !!')
                    return redirect("singup")
            else:
                messages.info(request, ' Both password are not same!!')
                return redirect("singup")

        else:
            messages.info(request, 'Captcha is incorrect  !!')
            print("chek captch")
            return render(request, "Mpost/singUp.html",data)





def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("yes")
            # succefully login
            messages.info(request, ' SignUp Done !!')
            return redirect('dashboard')
        else:
            print("no")
            messages.info(request, 'Check password and username !!')
            return redirect('login')
    else:
        return render(request, "Mpost/login.html")


def dashboard(request):
    if request.method== 'GET':
        data=Blog.objects.filter(user=request.user.id) # thsi is filter using user id

        print("i am id ",id)
        parse={'data':data,
               'media_url': settings.MEDIA_URL
               }


    return render(request,"Mpost/dashboard.html",parse)

def addPost(request):
    if request.method== 'POST':
        myfile = request.FILES.get('myfile')

        description = request.POST.get('desc')
        user=request.POST.get('user_id')
        privacy=request.POST.get('con')
        name=request.POST.get('name')
        print(user,myfile,description,privacy)
        blog=Blog(user=user,user_name=name, photo_main=myfile,description=description,privacy=privacy)

        blog.save()
        print("done")
        messages.info(request, 'Post s save !!')

    return render(request,"Mpost/addPost.html")
def allPost(request):
    if request.method=='POST':
        user=request.POST.get('find')
        find=Blog.objects.filter(user_name=user,privacy=False) # this will only show public data

        data={'find': find }
        return render(request, 'Mpost/allPost.html',data)
    else:
        if request.method=='GET':
            find=Blog.objects.filter(privacy=False)
            data={'find':find}
            messages.info(request, 'Showing all Post !!')
            return render(request, 'Mpost/allPost.html', data)
    return render(request,'Mpost/allPost.html')


def userLogout(request):
    logout(request)
    return HttpResponseRedirect("login")


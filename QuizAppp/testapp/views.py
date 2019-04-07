from django.shortcuts import render
from testapp.models import USER_LOGIN,User,USER_RESULT
from django.contrib.auth.hashers import make_password
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    messages.info(request, 'successfully Registered!')
    return render(request,'testapp/LoginPage.html')

def user_register(request):
    registered=False
    if request.method =='POST':
         if request.POST.get('psw')==request.POST.get('psw-repeat'):
             user_name1 = request.POST.get('username')
             pass_word1 = request.POST.get('psw')
             enc_password = make_password(pass_word1)
             user = User(username=user_name1, password=enc_password)
             user.email=request.POST.get('email')
             try:
                   user.save()
                   user_obj=USER_LOGIN(first_name=request.POST.get('First_Name'),last_name=request.POST.get('Last_Name') ,user_name=request.POST.get('username'),
                             pass_word=request.POST.get('psw'),email_id=request.POST.get('email'),gender=request.POST.get('gender')
                            )
                   user_obj.save()

                   registered = True
                   return index(request)
             except:
                   return HttpResponse("sorry username or email already exist please try with other one!")

         else:
            #messages.warning(request, 'Invalid credentials!')
              return HttpResponse("both passwords are not matched!")

    else:
         return render(request,'testapp/RegisterPage.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, "testapp/Qindex.html",{'user':user})
            else:
                return HttpResponse("Account Not Active")

        else:
            print("some tried to login and failed")
            print("email:{} and password :{}".format(username, password))
            messages.warning(request, 'Invalid credentials!')
            return render(request, "testapp/LoginPage.html")
            # return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'testapp/LoginPage.html')

def user_result(request):
    if request.method=='POST':
        user_obj=USER_LOGIN.objects.get(user_name=request.user)
        try:
            check=USER_RESULT.objects.get(user=user_obj)

        except:
            check=None

        var=0
        if request.POST.get('options1')=='Scripting':
            var=var+1
        if request.POST.get('options2')=='script':
            var=var+1
        if request.POST.get('options3')=='src':
            var=var+1
        if request.POST.get('options4')=='//':
            var=var+1
        if request.POST.get('options5')=='var':
            var=var+1

        if check is None:
            ob1=USER_RESULT(user=user_obj,result=var)
            ob1.save()
        else:
            check.result=var
            check.save()
        return render(request,'testapp/result_display.html',{'score':var})
    else:
        return render(request,'testapp/Qindex.html')
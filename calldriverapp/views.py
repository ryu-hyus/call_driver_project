import json
from urllib import request
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import MyUser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def CustomerLoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            print('인증 성공')
            login(request, user)
        else:
            print('인증 실패')
    return render(request, "customer/login.html")


@csrf_exempt
def SigUpView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)

        username = data.get('username')
        password = data.get('password')
        name = data.get('name')
        phone_number = data.get('phone_number')
        gear_type = data.get('gear_type', False)

        user = MyUser.objects.create_user(username, password, phone_number, gear_type)
        user.name = name
        user.phone_number = phone_number
        user.gear_type = gear_type
        user.save()
        return redirect("/customer/login/")

    return render(request, 'customer/signup.html')
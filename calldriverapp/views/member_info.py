import json
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from calldriverapp.models.customer import MyUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login

@method_decorator(csrf_exempt)
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password") 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if check_password(password, user.password):
                return render(request, 'customer/index.html')  # 로그인 성공시 연결 
        elif MyUser.DoesNotExist:
            return redirect('/customer/login.html')
        
    return render(request, "customer/login.html")


@method_decorator(csrf_exempt)
def sign_up(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        name = request.POST["name"]
        phone_number = request.POST["phone_number"]
        gear_type = request.POST["gear_type"]

        user = MyUser.objects.create_user(username, password, phone_number, gear_type)
        user.name = name
        user.phone_number = phone_number
        user.gear_type = gear_type
        user.save()
        return redirect("/customer/login/")

    return render(request, "customer/signup.html")

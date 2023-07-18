import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from calldriverapp.models.customer import MyUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as login
from django.contrib.auth.hashers import make_password


@method_decorator(csrf_exempt, name='dispatch')
class CustomerLoignView(View):
    def get(self, request):
        return render(request,'customer/login.html')

    def post(self, request):
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password") 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if check_password(password, user.password):
                    return render(request, 'customer/index.html')  # 로그인 성공시 연결            
            return HttpResponse("유저가 없습니다", status=500)
        else:
            return render(request, 'customer/login.html')




@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(View):
    def get(self, request):
        return render(request,'customer/signup.html')

    def post(self, request):
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            name = data.get("name")
            phone_number = data.get("phone_number")
            gear_type = data.get("gear_type")

            if not username:
                return HttpResponse('아이디를 입력해주세요.', status=400)
            
            password = phone_number[-4: ]
            hashed_password = make_password(password)
            user = MyUser.objects.create_user(username=username, password=password, phone_number=phone_number, gear_type=gear_type)
            user.name = name
            user.save()
            return redirect("/customer/login/")

        return render(request, "customer/signup.html")
    

@method_decorator(csrf_exempt, name='dispatch')
class StaffLoginView(View):
    def get(self, request):
        return render(request,'center/login.html')

    def post(self, request):
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password") 
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                if check_password(password, user.password):
                    return render(request, 'customer/index.html')  # 로그인 성공시 연결            
            return HttpResponse("유저가 없습니다", status=500)
        else:
            return render(request, 'customer/login.html')      
            
@method_decorator(csrf_exempt, name='dispatch')
class FindIdView(View):
    def get(self, request):
        return render(request, 'customer/find_id.html')
    
    def post(self, request):
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')

        try:
            user = MyUser.objects.get(name=name, phone_number=phone_number)
            return JsonResponse({ "username" : user.username })
        except MyUser.DoesNotExist:
            return JsonResponse({ "error" : "아이디를 찾을 수 없습니다."}, status=400 )
        

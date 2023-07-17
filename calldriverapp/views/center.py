import json
from django import forms
from django.http import ( HttpResponse, JsonResponse,)
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

class MainView(TemplateView):
    template_name = "center/home.html"



    

# class SuperuserLoginView(TemplateView):
#     template_name = "center/superuser_login_template.html"  

class CustomerListView(TemplateView):
    template_name = "center/customer_list_template.html"

class RealtimeOrderView(TemplateView):
    template_name = "center/realtime_order_template.html"

class TodayOrderView(TemplateView):
    template_name = "center/today_order_template.html"

class TotalOrderView(TemplateView):
    template_name = "center/total_order_template.html"

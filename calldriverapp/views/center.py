import json
from django import forms
from django.http import ( HttpResponse, JsonResponse,)
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

# 영업시작 후
class CustomerListView(LoginRequiredMixin, TemplateView):
    login_url = "/center/login/"
    template_name = "center/customer_list_template.html"

class RealtimeOrderView(LoginRequiredMixin, TemplateView):
    login_url = "/center/login/"
    template_name = "center/realtime_order_template.html"

class TodayOrderView(LoginRequiredMixin, TemplateView):
    login_url = "/center/login/"
    template_name = "center/today_order_template.html"

class TotalOrderView(LoginRequiredMixin, TemplateView):
    login_url = "/center/login/"
    template_name = "center/total_order_template.html"


# 영업시작 전 혹은 영업종료한 경우
class OffMainView(LoginRequiredMixin, TemplateView):
    login_url = "/center/login/"
    template_name = "center/offmain.html"
    
class OffCustomerView(LoginRequiredMixin, TemplateView):
    login_url = "/center/login/"
    template_name = "center/off_customer_list_template.html"
 
class OffTotalOrderView(LoginRequiredMixin, TemplateView):
    login_url = "/center/login/"
    template_name = "center/off_total_order_template.html"
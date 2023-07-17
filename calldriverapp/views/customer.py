from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "customer/index.html"

class OrderMainTemplateView(TemplateView):
    template_name = "customer/ordermain.html"

class OrderDetailTemplateView(TemplateView):
    template_name = "customer/orderdetail.html"

class OrderChangeTemplateView(TemplateView):
    template_name = "customer/orderchange.html"
    
class CustomerLoginView(TemplateView):
    template_name = "customer/login.html"

class SigUpView(TemplateView):
    template_name = "customer/signup.html"
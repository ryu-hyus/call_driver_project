from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "customer/index.html"

class CustomerLoginView(TemplateView):
    template_name = "customer/login.html"

class SigUpView(TemplateView):
    template_name = "customer/signup.html"
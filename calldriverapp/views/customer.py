from django.views.generic import TemplateView

from calldriverapp.models import OperationOnOff


class HomeTemplateView(TemplateView):
    template_name = "customer/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        operation_onoff = OperationOnOff.objects.order_by('-id').first().operation_onoff

        context["disable_button"] = operation_onoff
        return context


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

class PricePageView(TemplateView):
    template_name = "customer/pricepage.html"

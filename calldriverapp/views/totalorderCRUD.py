import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from calldriverapp.models.customer import MyUser
from calldriverapp.models.orderdata import OrderData
from calldriverapp.models.operation import OperationDay
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class TotalOrderGetView(View):

    # 조회
    def get(self, request, pk=None):
        if pk is not None:
            orderdata = get_object_or_404(OrderData, id=pk)
            orderlist = [self.modify_orderdata(orderdata)]
            return JsonResponse(orderlist, safe=False)
        else:
            orderlist = OrderData.objects.all()
            orderlist = [self.modify_orderdata(orderdata) for orderdata in orderlist]
            return JsonResponse(orderlist, safe=False)

    def modify_orderdata(self, orderdata):
        order_dict = orderdata.__dict__
        order_dict.pop("_state")  # Django 모델에서 추가된 '_state' 필드를 제거
        customer = MyUser.objects.get(id=orderdata.customer_id)
        order_dict["phone_number"] = customer.phone_number
        order_dict["gear_type"] = customer.gear_type
        order_dict["username"] = customer.username
        return order_dict

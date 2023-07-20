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
class RealtimeOrderGetView(View):
    # 조회
    def get(self, request):
        operationday = OperationDay.objects.filter(id=1).values().first()
        orderdata = OrderData.objects.filter(
            order_type=True, is_hide=False, operation_day=operationday['operation_day']).values()
        orderlist = list(orderdata)

        for i in orderlist:
            phonenumber = MyUser.objects.filter(
                id=i['customer_id']).values().first()['phone_number']
            i['phone_number'] = phonenumber

        return JsonResponse(orderlist, safe=False)

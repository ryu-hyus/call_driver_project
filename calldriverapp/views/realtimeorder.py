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

            geartype = MyUser.objects.filter(
                id=i['customer_id']).values().first()['gear_type']
            i['gear_type'] = geartype

        return JsonResponse(orderlist, safe=False)
    
    # 수정
    def put(self, request, pk):
        orderlist = get_object_or_404(OrderData, pk=pk)
        data = json.loads(request.body)
    
        orderlist.order_type = data.get("order_type") or orderlist.order_type
        orderlist.is_hide = data.get("is_hide") or orderlist.is_hide
    
        # OrderConfirm 메서드 호출
        if orderlist.order_type == False:
            orderlist.OrderConfirm()
    
        orderlist.save()
        return JsonResponse(data)

      

# 16번째 줄 : id=1 전체 데이터 중 첫 번째, first()는 filter된 것 중 첫 번째 (약간 개발자 매너?로 적으신 듯)
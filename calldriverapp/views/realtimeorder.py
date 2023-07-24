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
    def get(self, request, pk=None):
        operationday = OperationDay.objects.filter(id=1).values().first()
        orderdata = OrderData.objects.filter(
            order_type=True, is_hide=False, 
            operation_day=operationday["operation_day"]).values()
        orderlist = list(orderdata)

        # 단건조회
        if pk is not None:
            for order in orderlist:
                if order['id'] == pk:
                    phonenumber = (
                        MyUser.objects.filter(id=order["customer_id"])
                        .values()
                        .first()["phone_number"]
                    )
                    order["phone_number"] = phonenumber

                    geartype = (
                        MyUser.objects.filter(id=order["customer_id"])
                        .values()
                        .first()["gear_type"]
                    )
                    order["gear_type"] = geartype

                    return JsonResponse(order)

            # 해당 pk의 주문을 찾지 못한 경우
            return JsonResponse({"error": "해당 주문을 찾을 수 없습니다."}, status=404)

        # 다건조회
        else:
            for i in orderlist:
                phonenumber = (
                    MyUser.objects.filter(id=i["customer_id"])
                    .values()
                    .first()["phone_number"]
                )
                i["phone_number"] = phonenumber

                geartype = (
                    MyUser.objects.filter(id=i["customer_id"]).values().first()["gear_type"]
                )
                i["gear_type"] = geartype

            return JsonResponse(orderlist, safe=False)
            

    # 수정
    def put(self, request, pk):
        orderlist = get_object_or_404(OrderData, pk=pk)
        data = json.loads(request.body)

        orderlist.order_type = data.get("order_type") or orderlist.order_type
        orderlist.is_hide = data.get("is_hide") or orderlist.is_hide

        # OrderConfirm 메서드 호출
        if orderlist.order_type == True:
            orderlist.OrderConfirm()

        if orderlist.is_hide == False:
            orderlist.OrderHide()

        orderlist.save()

        return JsonResponse(data)



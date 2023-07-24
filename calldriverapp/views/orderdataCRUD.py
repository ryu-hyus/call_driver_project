import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from calldriverapp.models.orderdata import OrderData
from calldriverapp.models.operation import OperationDay
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class OrderdataView(View):
    #조회
    def get(self, request, pk=None):
        #단건조회
        if pk is not None:

            orderdata = OrderData.objects.filter(id=pk).values().first()

            if not orderdata:
                return JsonResponse({"error": "Order not found"}, status=404)
            return JsonResponse(orderdata)
        # 다건조회
        else:
            orderdata = OrderData.objects.all().values()
            return JsonResponse(list(orderdata) , safe=False)
    
    # 수정
    def put(self, request, pk):
        orderdata = get_object_or_404(OrderData, pk=pk)
        data = json.loads(request.body)

        orderdata.start_address = data.get("start_address") or orderdata.start_address
        orderdata.end_address = data.get("end_address") or orderdata.end_address
        orderdata.start_section = data.get("start_section") or orderdata.start_section
        orderdata.end_section = data.get("end_section") or orderdata.end_section
        orderdata.order_kind = data.get("order_kind") or orderdata.order_kind
        orderdata.order_type = data.get("order_type") or orderdata.order_type
        orderdata.is_hide = data.get("is_hide") or orderdata.is_hide
        orderdata.calculated_price = data.get("calculated_price") or orderdata.calculated_price

        orderdata.save()
        return JsonResponse(data)

    # 등록
    def post(self, request):
        data = json.loads(request.body)
        center_day = OperationDay.objects.all()[0].operation_day

        p = OrderData(
            start_address=data.get("start_address"),
            end_address=data.get("end_address"),
            start_section=data.get("start_section"),
            end_section=data.get("end_section"),
            customer_id=data.get("customer_id"),
            calculated_price = data.get("calculated_price"),
            operation_day = center_day,
        )
        p.save()
        return HttpResponse(status=200)

class CustomerOrderView(View):
    #조회
    def get(self, request, pk):
        #유저 id로 조회
        center_day = OperationDay.objects.all()[0].operation_day
        orderdata = OrderData.objects.filter(customer_id=pk, operation_day = center_day, is_deleted = False).exclude(order_kind = 'cancel', order_type = False).values()

        if not orderdata:
            return JsonResponse({"error": "Order not found"}, status=404)
        
        return JsonResponse(list(orderdata) , safe=False)


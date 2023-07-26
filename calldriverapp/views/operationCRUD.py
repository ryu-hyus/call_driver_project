import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from calldriverapp.models.operation import OperationDay, OperationOnOff


@method_decorator(csrf_exempt, name="dispatch")
class OperationOnOffView(View):
    def get(self, request):
        operation_onoff = OperationOnOff.objects.order_by('-id').first().operation_onoff
        return JsonResponse({"operation_onoff": operation_onoff})

    def post(self, request):
        data = json.loads(request.body)
        operation_onoff_value = data.get("operation_onoff")
        
        if operation_onoff_value == True:
            operation_onoff_value = operation_onoff_value
        else:
            operation_onoff_value = False

        operation_onoff = OperationOnOff(operation_onoff=operation_onoff_value)
        operation_onoff.save()
        return HttpResponse(status=200)

    # 수정
    # def put(self, request):
    #     data = json.loads(request.body)
    #     operation_onoff_value = data.get("operation_onoff")

    #     if operation_onoff_value == True:
    #         operation_onoff_value.set_off()
    #     else:
    #         operation_onoff_value.set_on()

    #     operation_onoff_value.save()
    #     return HttpResponse(status=200)
    
@method_decorator(csrf_exempt, name="dispatch")
class OperationDaySetView(View):
    def put(self, request):
        operationday = OperationDay.objects.filter(id=1).first()
        operationday.set_day()
        operationday.save()
        return HttpResponse(status=200)
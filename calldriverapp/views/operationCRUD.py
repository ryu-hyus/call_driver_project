import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from calldriverapp.models.operation import OperationOnOff


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
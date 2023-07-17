import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from calldriverapp.models.addresshistory import AddressHistory


@method_decorator(csrf_exempt, name="dispatch")
class AddresshistorydataView(View):
    #커스토머 id로 조회
    def get(self, request, pk):
        
        addressdata = AddressHistory.objects.filter(customer_id=pk).values()
        if not addressdata:
            return JsonResponse({"error": "Order not found"}, status=404)
        return JsonResponse(list(addressdata) , safe=False)
    
    # 등록
    def post(self, request, pk):
        data = json.loads(request.body)

        p = AddressHistory(
            raw_address=data.get("raw_address"),
            trans_address=data.get("trans_address"),
            section_name=data.get("section_name"),
            address_type=data.get("address_type"),
            customer_id = pk,
        )
        p.save()
        return HttpResponse(status=200)

@method_decorator(csrf_exempt, name="dispatch")
class AddresshistorydeleteView(View):
    # 삭제
    def put(self, request, pk):
        addressdata = get_object_or_404(AddressHistory, pk=pk)

        addressdata.is_deleted = True

        addressdata.save()
        return HttpResponse(status=200)

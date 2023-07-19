import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from calldriverapp.models.pricetable import PriceTable
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class PriceTableView(View):
    # 조회
    def get(self, request, ss, es):
        # ss: start_section, es : end_section
        pricedata = PriceTable.objects.filter(start_section=ss, end_section=es).values().first()

        if not pricedata:
            return JsonResponse({"error": "Order not found"}, status=404)

        return JsonResponse({"calculated_price": pricedata['calculated_price']})
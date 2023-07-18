from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from calldriverapp.models.customer import MyUser

@method_decorator(csrf_exempt, name="dispatch")
class CustomerInfoView(View):
    #조회
    def get(self, request, pk=None):
        #단건조회
        if pk is not None:

            myuser = MyUser.objects.filter(id=pk).values().first()

            if not myuser:
                return JsonResponse({"error": "Order not found"}, status=404)
            return JsonResponse(myuser)
        # 다건조회
        else:
            myuser = MyUser.objects.all().values()
            return JsonResponse(list(myuser) , safe=False)
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from master_service.api_category_conn import finance, messaging
from master_service.serializers import ReceiveRoutineSerializer

# Logic for handling incoming requests
from django.views.decorators.csrf import csrf_exempt

#
#
# @csrf_exempt
# def receive_routine(request):
#     if request.method == "POST":
#         # TODO: 1) create a object (or array) through parsing the incoming routine
#         # TODO: 2) extract different activities
#         # TODO: 3) order them and perform necessary API calls to respective API Category through api_category_conn.
#         # example:
#         finance.get_stockprice_for_company('adidas')
#         return JsonResponse({'success': 'yes'}, status=200)
#     else:
#         return JsonResponse({'success': 'request received. Implement routine extraction method'}, status=200)

class ReceiveRoutineViewSet(viewsets.ViewSet):
    serializer_class = ReceiveRoutineSerializer

    def backend_info(request):
        return render(request, 'backend_info.html', {})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        deserialized_data=serializer.validated_data

        if request.method == "POST":
            finance.get_stockprice_for_company(deserialized_data["company"])
            return JsonResponse({'success': 'yes'}, status=200)
        else:
            return JsonResponse({'success': 'request received. Implement routine extraction method'}, status=200)


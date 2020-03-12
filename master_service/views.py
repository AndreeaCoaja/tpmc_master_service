import json

from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging

from .api_category_conn import finance, messaging
from .environment.env import AllCategoryNames


def backend_info(request):
    return render(request, 'backend_info.html', {})


@csrf_exempt
def receive_routine(request):
    if request.method == "POST":
        # TODO: 1) create a object (or array) through parsing the incoming routine
        # TODO: 2) extract different activities and store them in e.g. an array
        activity_array = []

        # Mocked Data
        financing_activity = {
            "type": "FINANCING",
            "purpose": "GET_SPECIFIC_STOCKPRICE",
            "company_name": "adidas"
        }
        financing_activity = json.dumps(financing_activity)  # Create JSON

        messaging_activity = {
            "type": "MESSAGING",
            "purpose": "SEND_EMAIL",
            "to": "adidas",
            "subject": "Hello from the other side"
        }
        messaging_activity = json.dumps(messaging_activity)  # Create JSON

        activity_array.append(json.loads(financing_activity))  # Create Python DICT and append to activity array
        activity_array.append(json.loads(messaging_activity))  # Create Python DICT and append to activity array

        last_response = ""
        for phase in activity_array:
            # for activity in phase:  # Consider this for granularity --> simplify by ignoring simultaneous activities?
            if phase['type'] == AllCategoryNames.finance.value:
                last_response = finance.use(phase, last_response)
            if phase['type'] == AllCategoryNames.messaging.value:
                last_response = messaging.use(phase, last_response)

            return JsonResponse({'success': 'POST request done.'}, status=200)

    else:
        return JsonResponse({'success': 'GET request received.'}, status=200)

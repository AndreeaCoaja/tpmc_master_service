from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from master_service.api_category_conn import finance, messaging
from master_service.serializers import ReceiveRoutineSerializer
from master_service.parser import parseJSON, transformationAlgorithm


# Logic for handling incoming requests

class ReceiveRoutineViewSet(viewsets.ViewSet):
    serializer_class = ReceiveRoutineSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        deserialized_data = serializer.validated_data

        my_json = parseJSON.parse_json_routines(deserialized_data["routine"])

        transformationAlgorithm.transform(my_json)

        return Response({'success': 'yes'})

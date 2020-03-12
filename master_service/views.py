from rest_framework import viewsets
from rest_framework.response import Response

from master_service.serializers import ReceiveRoutineSerializer
from master_service.user_routine.parser.parse_json import parse_json_routines
from master_service.user_routine.parser.transformation_algorithm import transform


# Logic for handling incoming requests

class ReceiveRoutineViewSet(viewsets.ViewSet):
    serializer_class = ReceiveRoutineSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        deserialized_data = serializer.validated_data

        my_json = parse_json_routines(deserialized_data["routine"])

        routine = transform(my_json)

        return Response({'success': 'yes'})

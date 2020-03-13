from rest_framework import serializers


class ReceiveRoutineSerializer(serializers.Serializer):
    routine = serializers.JSONField(required=True)

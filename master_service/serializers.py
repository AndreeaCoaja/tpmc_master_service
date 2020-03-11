from rest_framework import serializers


class ReceiveRoutineSerializer(serializers.Serializer):
    company = serializers.CharField()
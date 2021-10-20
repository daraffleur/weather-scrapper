from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    day = serializers.CharField()
    description = serializers.CharField()
    temperature = serializers.CharField()

from rest_framework import serializers


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    business_name = serializers.CharField()
    address = serializers.CharField(allow_blank=True)
    phone_number = serializers.CharField(allow_blank=True)

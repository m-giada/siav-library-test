from rest_framework import serializers



class PaginationSerializer(serializers.Serializer):
    page = serializers.IntegerField()
    page_size = serializers.IntegerField()
    total_count = serializers.IntegerField()
    results = serializers.ListField()


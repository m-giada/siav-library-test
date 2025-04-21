from rest_framework import serializers


class BookDeserializer(serializers.Serializer):
    title = serializers.CharField()
    author_ids = serializers.ListField(child=serializers.IntegerField())
    publisher_id = serializers.IntegerField()
    publication_year = serializers.IntegerField(required=False)
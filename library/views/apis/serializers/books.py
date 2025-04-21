from rest_framework import serializers

from library.views.apis.serializers.authors import AuthorSerializer
from library.views.apis.serializers.pagination import PaginationSerializer
from library.views.apis.serializers.publishers import PublisherSerializer


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    publisher = PublisherSerializer()
    authors = serializers.ListField(child=AuthorSerializer())
    publication_year = serializers.IntegerField(allow_null=True)


class PaginatedBookListSerializer(PaginationSerializer):
    results = BookSerializer(many=True)
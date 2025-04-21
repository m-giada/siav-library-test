from rest_framework import serializers

from library.constants import PAGINATION_MIN_PAGE_VALUE, PAGINATION_DEFAULT_PAGE_VALUE, \
    PAGINATION_DEFAULT_PAGE_SIZE_VALUE


class PaginationDeserializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=PAGINATION_DEFAULT_PAGE_VALUE, min_value=PAGINATION_MIN_PAGE_VALUE)
    page_size = serializers.IntegerField(required=False, default=PAGINATION_DEFAULT_PAGE_SIZE_VALUE)
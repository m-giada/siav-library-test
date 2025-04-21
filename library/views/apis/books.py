from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from library.views.apis.deserializers.books import BookDeserializer
from library.views.apis.deserializers.pagination import PaginationDeserializer
from library.views.apis.serializers.books import BookSerializer, PaginatedBookListSerializer
from library.requests.books import CreateBookRequest, ListBooksRequest
from library.usecases.list_books import ListBooksUseCase
from library.usecases.save_book import SaveBookUseCase


class BooksAPIView(APIView):

    def post(self, request):
        deserializer = BookDeserializer(data=request.data)
        deserializer.is_valid(raise_exception=True)

        book_request = CreateBookRequest(**deserializer.validated_data)
        try:
            book = SaveBookUseCase.execute(request=book_request)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)


    def get(self, request):
        deserializer = PaginationDeserializer(data=request.query_params)
        deserializer.is_valid(raise_exception=True)

        list_request = ListBooksRequest(**deserializer.validated_data)
        paginated_books = ListBooksUseCase.execute(request=list_request)
        return Response(PaginatedBookListSerializer(paginated_books).data, status=status.HTTP_200_OK)

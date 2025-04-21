from typing import List, Optional

from django.db import transaction

from library.dtos.authors import AuthorDTO
from library.dtos.books import BookDTO
from library.dtos.publishers import PublisherDTO
from library.models import Book, Author, Publisher
from library.requests.authors import CreateAuthorRequest
from library.requests.books import CreateBookRequest, ListBooksRequest
from library.requests.publishers import CreatePublisherRequest


class BooksRepository:

    @staticmethod
    def create_author(author_request: CreateAuthorRequest) -> AuthorDTO:
        author = Author.objects.create(
            first_name=author_request.first_name,
            last_name=author_request.last_name,
        )
        return AuthorDTO.from_orm(author)

    @staticmethod
    def _get_authors_models(author_ids: List[int]) -> List[Author]:
        return list(Author.objects.filter(id__in=author_ids))


    @staticmethod
    def create_publisher(publisher_request: CreatePublisherRequest) -> PublisherDTO:
        publisher = Publisher.objects.create(
            business_name=publisher_request.business_name,
            address=publisher_request.address,
            phone_number=publisher_request.phone_number,
        )
        return PublisherDTO.from_orm(publisher)

    @staticmethod
    def get_publisher_by_id(publisher_id: int) -> Optional[PublisherDTO]:
        try:
            publisher = Publisher.objects.get(id=publisher_id)
        except Publisher.DoesNotExist:
            return None
        return PublisherDTO.from_orm(publisher)

    @staticmethod
    def get_books(list_request: ListBooksRequest) -> tuple[int, List[BookDTO]]:
        queryset = Book.objects.all()
        total_count = queryset.count()

        offset = (list_request.page - 1) * list_request.page_size
        limit = list_request.page_size
        books_list = list(queryset[offset:offset+limit])
        return total_count, BookDTO.from_orm_list(books_list)

    @classmethod
    @transaction.atomic
    def create_book(cls, book_request: CreateBookRequest) -> BookDTO:
        if cls.get_publisher_by_id(book_request.publisher_id) is None:
            raise Exception(f"publisher id {book_request.publisher_id} not found")

        book = Book.objects.create(
            title=book_request.title,
            publication_year=book_request.publication_year,
            publisher_id=book_request.publisher_id,
        )
        authors = cls._get_authors_models(author_ids=book_request.author_ids)
        book.authors.add(*authors)
        return BookDTO.from_orm(book)


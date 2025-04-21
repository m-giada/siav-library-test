from library.dtos.books import BookDTO
from library.repositories.books import BooksRepository
from library.requests.books import CreateBookRequest


class SaveBookUseCase:

    @staticmethod
    def execute(request: CreateBookRequest) -> BookDTO:
        return BooksRepository.create_book(book_request=request)

from library.dtos.pagination import PaginationDTO
from library.repositories.books import BooksRepository
from library.requests.books import ListBooksRequest


class ListBooksUseCase:

    @staticmethod
    def execute(request: ListBooksRequest) -> PaginationDTO:
        total_count, books = BooksRepository.get_books(list_request=request)
        return PaginationDTO(
            total_count=total_count,
            page=request.page,
            page_size=request.page_size,
            results=books,
        )
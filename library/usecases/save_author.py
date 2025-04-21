from library.dtos.authors import AuthorDTO
from library.repositories.books import BooksRepository
from library.requests.authors import CreateAuthorRequest


class SaveAuthorUseCase:

    @staticmethod
    def execute(request: CreateAuthorRequest) -> AuthorDTO:
        return BooksRepository.create_author(author_request=request)
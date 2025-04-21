from library.dtos.publishers import PublisherDTO
from library.repositories.books import BooksRepository
from library.requests.publishers import CreatePublisherRequest


class SavePublisherUseCase:

    @staticmethod
    def execute(request: CreatePublisherRequest) -> PublisherDTO:
        return BooksRepository.create_publisher(publisher_request=request)

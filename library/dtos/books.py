from dataclasses import dataclass
from typing import List

from library.dtos.authors import AuthorDTO
from library.dtos.publishers import PublisherDTO


@dataclass
class BookDTO:
    id: int
    title: str
    authors: List[AuthorDTO]
    publisher: PublisherDTO
    publication_year: int = None

    @classmethod
    def from_orm(cls, orm):
        return cls(
            id=orm.id,
            title=orm.title,
            authors=AuthorDTO.from_orm_list(orm.authors.all()),
            publisher=PublisherDTO.from_orm(orm.publisher),
            publication_year=orm.publication_year,
        )

    @classmethod
    def from_orm_list(cls, orm_list):
        return [cls.from_orm(book) for book in orm_list]

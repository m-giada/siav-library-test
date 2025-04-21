from dataclasses import dataclass
from typing import List


@dataclass
class CreateBookRequest:
    title: str
    author_ids: List[int]
    publisher_id: int
    publication_year: int = None


@dataclass
class ListBooksRequest:
    page: int = 1
    page_size: int = 50

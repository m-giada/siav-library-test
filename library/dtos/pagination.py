from dataclasses import dataclass
from typing import List, Any

from library.constants import PAGINATION_DEFAULT_PAGE_SIZE_VALUE, PAGINATION_DEFAULT_PAGE_VALUE


@dataclass
class PaginationDTO:
    total_count: int
    results: List[Any]
    page: int = PAGINATION_DEFAULT_PAGE_VALUE
    page_size: int = PAGINATION_DEFAULT_PAGE_SIZE_VALUE
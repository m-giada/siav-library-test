from dataclasses import dataclass


@dataclass
class CreateAuthorRequest:
    first_name: str
    last_name: str

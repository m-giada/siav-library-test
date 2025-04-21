from dataclasses import dataclass


@dataclass
class CreatePublisherRequest:
    business_name: str
    address: str = ""
    phone_number: str = ""
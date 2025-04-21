from dataclasses import dataclass


@dataclass
class PublisherDTO:
    id: int
    business_name: str
    address: str = ""
    phone_number: str = ""

    @classmethod
    def from_orm(cls, orm):
        return cls(
            id=orm.id,
            business_name=orm.business_name,
            address=orm.address,
            phone_number=orm.phone_number,
        )
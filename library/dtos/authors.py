from dataclasses import dataclass


@dataclass
class AuthorDTO:
    id: int
    first_name: str
    last_name: str

    @classmethod
    def from_orm(cls, orm):
        return cls(
            id=orm.id,
            first_name=orm.first_name,
            last_name=orm.last_name,
        )

    @classmethod
    def from_orm_list(cls, orm_list):
        return [cls.from_orm(author) for author in orm_list]
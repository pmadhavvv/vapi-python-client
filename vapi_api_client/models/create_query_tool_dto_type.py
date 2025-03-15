from enum import Enum


class CreateQueryToolDTOType(str, Enum):
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)

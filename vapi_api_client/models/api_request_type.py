from enum import Enum


class ApiRequestType(str, Enum):
    APIREQUEST = "apiRequest"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class MakeCredentialProvider(str, Enum):
    MAKE = "make"

    def __str__(self) -> str:
        return str(self.value)

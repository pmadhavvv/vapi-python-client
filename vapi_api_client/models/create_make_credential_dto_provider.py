from enum import Enum


class CreateMakeCredentialDTOProvider(str, Enum):
    MAKE = "make"

    def __str__(self) -> str:
        return str(self.value)

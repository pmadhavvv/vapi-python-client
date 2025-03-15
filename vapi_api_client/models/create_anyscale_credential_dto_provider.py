from enum import Enum


class CreateAnyscaleCredentialDTOProvider(str, Enum):
    ANYSCALE = "anyscale"

    def __str__(self) -> str:
        return str(self.value)

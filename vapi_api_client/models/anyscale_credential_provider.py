from enum import Enum


class AnyscaleCredentialProvider(str, Enum):
    ANYSCALE = "anyscale"

    def __str__(self) -> str:
        return str(self.value)

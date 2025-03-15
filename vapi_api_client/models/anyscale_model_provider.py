from enum import Enum


class AnyscaleModelProvider(str, Enum):
    ANYSCALE = "anyscale"

    def __str__(self) -> str:
        return str(self.value)

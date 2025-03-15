from enum import Enum


class NeuphonicCredentialProvider(str, Enum):
    NEUPHONIC = "neuphonic"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class CreateNeuphonicCredentialDTOProvider(str, Enum):
    NEUPHONIC = "neuphonic"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class CreateHumeCredentialDTOProvider(str, Enum):
    HUME = "hume"

    def __str__(self) -> str:
        return str(self.value)

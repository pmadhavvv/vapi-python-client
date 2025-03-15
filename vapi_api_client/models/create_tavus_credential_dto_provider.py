from enum import Enum


class CreateTavusCredentialDTOProvider(str, Enum):
    TAVUS = "tavus"

    def __str__(self) -> str:
        return str(self.value)

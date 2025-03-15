from enum import Enum


class CreateMistralCredentialDTOProvider(str, Enum):
    MISTRAL = "mistral"

    def __str__(self) -> str:
        return str(self.value)

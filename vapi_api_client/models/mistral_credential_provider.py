from enum import Enum


class MistralCredentialProvider(str, Enum):
    MISTRAL = "mistral"

    def __str__(self) -> str:
        return str(self.value)

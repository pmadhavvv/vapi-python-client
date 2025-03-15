from enum import Enum


class CreateInflectionAICredentialDTOProvider(str, Enum):
    INFLECTION_AI = "inflection-ai"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class CreateOpenAICredentialDTOProvider(str, Enum):
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)

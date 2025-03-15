from enum import Enum


class CreateTogetherAICredentialDTOProvider(str, Enum):
    TOGETHER_AI = "together-ai"

    def __str__(self) -> str:
        return str(self.value)

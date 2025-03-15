from enum import Enum


class CreateRimeAICredentialDTOProvider(str, Enum):
    RIME_AI = "rime-ai"

    def __str__(self) -> str:
        return str(self.value)

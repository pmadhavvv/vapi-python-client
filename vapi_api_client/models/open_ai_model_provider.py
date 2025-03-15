from enum import Enum


class OpenAIModelProvider(str, Enum):
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)

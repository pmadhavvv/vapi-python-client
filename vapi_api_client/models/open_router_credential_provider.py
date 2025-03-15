from enum import Enum


class OpenRouterCredentialProvider(str, Enum):
    OPENROUTER = "openrouter"

    def __str__(self) -> str:
        return str(self.value)

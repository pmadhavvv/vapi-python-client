from enum import Enum


class CreateOpenRouterCredentialDTOProvider(str, Enum):
    OPENROUTER = "openrouter"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class AnthropicCredentialProvider(str, Enum):
    ANTHROPIC = "anthropic"

    def __str__(self) -> str:
        return str(self.value)

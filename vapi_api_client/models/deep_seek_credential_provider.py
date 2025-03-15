from enum import Enum


class DeepSeekCredentialProvider(str, Enum):
    DEEP_SEEK = "deep-seek"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class XAiCredentialProvider(str, Enum):
    XAI = "xai"

    def __str__(self) -> str:
        return str(self.value)

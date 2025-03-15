from enum import Enum


class LangfuseCredentialProvider(str, Enum):
    LANGFUSE = "langfuse"

    def __str__(self) -> str:
        return str(self.value)

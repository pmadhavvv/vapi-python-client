from enum import Enum


class CreateLangfuseCredentialDTOProvider(str, Enum):
    LANGFUSE = "langfuse"

    def __str__(self) -> str:
        return str(self.value)

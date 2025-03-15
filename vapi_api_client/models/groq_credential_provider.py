from enum import Enum


class GroqCredentialProvider(str, Enum):
    GROQ = "groq"

    def __str__(self) -> str:
        return str(self.value)

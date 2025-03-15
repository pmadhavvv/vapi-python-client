from enum import Enum


class CreateGroqCredentialDTOProvider(str, Enum):
    GROQ = "groq"

    def __str__(self) -> str:
        return str(self.value)

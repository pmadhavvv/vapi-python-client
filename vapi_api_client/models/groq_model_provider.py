from enum import Enum


class GroqModelProvider(str, Enum):
    GROQ = "groq"

    def __str__(self) -> str:
        return str(self.value)

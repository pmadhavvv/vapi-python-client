from enum import Enum


class TextContentType(str, Enum):
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)

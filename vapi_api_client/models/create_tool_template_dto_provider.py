from enum import Enum


class CreateToolTemplateDTOProvider(str, Enum):
    FUNCTION = "function"
    GOHIGHLEVEL = "gohighlevel"
    MAKE = "make"

    def __str__(self) -> str:
        return str(self.value)

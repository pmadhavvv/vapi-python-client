from enum import Enum


class UpdateToolTemplateDTOProvider(str, Enum):
    FUNCTION = "function"
    GOHIGHLEVEL = "gohighlevel"
    MAKE = "make"

    def __str__(self) -> str:
        return str(self.value)

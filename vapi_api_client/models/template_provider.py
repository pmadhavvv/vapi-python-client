from enum import Enum


class TemplateProvider(str, Enum):
    FUNCTION = "function"
    GOHIGHLEVEL = "gohighlevel"
    MAKE = "make"

    def __str__(self) -> str:
        return str(self.value)

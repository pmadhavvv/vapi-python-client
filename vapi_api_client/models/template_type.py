from enum import Enum


class TemplateType(str, Enum):
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)

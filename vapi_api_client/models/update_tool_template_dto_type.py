from enum import Enum


class UpdateToolTemplateDTOType(str, Enum):
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class AssistantHookFilterType(str, Enum):
    ONEOF = "oneOf"

    def __str__(self) -> str:
        return str(self.value)

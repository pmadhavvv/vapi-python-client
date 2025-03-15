from enum import Enum


class AssistantHooksOn(str, Enum):
    CALL_ENDING = "call.ending"

    def __str__(self) -> str:
        return str(self.value)

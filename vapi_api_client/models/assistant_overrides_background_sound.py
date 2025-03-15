from enum import Enum


class AssistantOverridesBackgroundSound(str, Enum):
    OFF = "off"
    OFFICE = "office"

    def __str__(self) -> str:
        return str(self.value)

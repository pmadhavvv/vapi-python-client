from enum import Enum


class NeetsVoicePresetVoiceOptions(str, Enum):
    VITS = "vits"

    def __str__(self) -> str:
        return str(self.value)

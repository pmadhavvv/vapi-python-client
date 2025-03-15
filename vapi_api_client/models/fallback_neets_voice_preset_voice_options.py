from enum import Enum


class FallbackNeetsVoicePresetVoiceOptions(str, Enum):
    VITS = "vits"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class FallbackLMNTVoicePresetVoiceOptions(str, Enum):
    DANIEL = "daniel"
    LILY = "lily"

    def __str__(self) -> str:
        return str(self.value)

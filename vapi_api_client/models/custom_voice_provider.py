from enum import Enum


class CustomVoiceProvider(str, Enum):
    CUSTOM_VOICE = "custom-voice"

    def __str__(self) -> str:
        return str(self.value)

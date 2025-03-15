from enum import Enum


class CustomTranscriberProvider(str, Enum):
    CUSTOM_TRANSCRIBER = "custom-transcriber"

    def __str__(self) -> str:
        return str(self.value)

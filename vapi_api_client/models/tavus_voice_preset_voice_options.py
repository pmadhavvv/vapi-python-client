from enum import Enum


class TavusVoicePresetVoiceOptions(str, Enum):
    R52DA2535A = "r52da2535a"

    def __str__(self) -> str:
        return str(self.value)

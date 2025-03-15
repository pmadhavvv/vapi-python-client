from enum import Enum


class RimeAIVoiceProvider(str, Enum):
    RIME_AI = "rime-ai"

    def __str__(self) -> str:
        return str(self.value)

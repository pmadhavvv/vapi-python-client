from enum import Enum


class GeminiMultimodalLivePrebuiltVoiceConfigVoiceName(str, Enum):
    AOEDE = "Aoede"
    CHARON = "Charon"
    FENRIR = "Fenrir"
    KORE = "Kore"
    PUCK = "Puck"

    def __str__(self) -> str:
        return str(self.value)

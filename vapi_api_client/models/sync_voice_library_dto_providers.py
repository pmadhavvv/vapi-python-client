from enum import Enum


class SyncVoiceLibraryDTOProviders(str, Enum):
    AZURE = "azure"
    CARTESIA = "cartesia"
    CUSTOM_VOICE = "custom-voice"
    DEEPGRAM = "deepgram"
    HUME = "hume"
    LMNT = "lmnt"
    NEETS = "neets"
    NEUPHONIC = "neuphonic"
    OPENAI = "openai"
    PLAYHT = "playht"
    RIME_AI = "rime-ai"
    SMALLEST_AI = "smallest-ai"
    TAVUS = "tavus"
    VALUE_1 = "11labs"
    VAPI = "vapi"

    def __str__(self) -> str:
        return str(self.value)

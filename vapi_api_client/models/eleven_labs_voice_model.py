from enum import Enum


class ElevenLabsVoiceModel(str, Enum):
    ELEVEN_FLASH_V2 = "eleven_flash_v2"
    ELEVEN_FLASH_V2_5 = "eleven_flash_v2_5"
    ELEVEN_MONOLINGUAL_V1 = "eleven_monolingual_v1"
    ELEVEN_MULTILINGUAL_V2 = "eleven_multilingual_v2"
    ELEVEN_TURBO_V2 = "eleven_turbo_v2"
    ELEVEN_TURBO_V2_5 = "eleven_turbo_v2_5"

    def __str__(self) -> str:
        return str(self.value)

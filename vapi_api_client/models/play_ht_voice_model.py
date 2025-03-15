from enum import Enum


class PlayHTVoiceModel(str, Enum):
    PLAY3_0_MINI = "Play3.0-mini"
    PLAYDIALOG = "PlayDialog"
    PLAYHT2_0 = "PlayHT2.0"
    PLAYHT2_0_TURBO = "PlayHT2.0-turbo"

    def __str__(self) -> str:
        return str(self.value)

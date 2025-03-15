from enum import Enum


class ElevenLabsVoicePresetVoiceOptions(str, Enum):
    ANDREA = "andrea"
    BURT = "burt"
    DREW = "drew"
    JOSEPH = "joseph"
    MARISSA = "marissa"
    MARK = "mark"
    MATILDA = "matilda"
    MRB = "mrb"
    MYRA = "myra"
    PAUL = "paul"
    PAULA = "paula"
    PHILLIP = "phillip"
    RYAN = "ryan"
    SARAH = "sarah"
    STEVE = "steve"

    def __str__(self) -> str:
        return str(self.value)

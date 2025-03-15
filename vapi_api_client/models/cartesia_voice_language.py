from enum import Enum


class CartesiaVoiceLanguage(str, Enum):
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    HI = "hi"
    IT = "it"
    JA = "ja"
    KO = "ko"
    NL = "nl"
    PL = "pl"
    PT = "pt"
    RU = "ru"
    SV = "sv"
    TR = "tr"
    ZH = "zh"

    def __str__(self) -> str:
        return str(self.value)

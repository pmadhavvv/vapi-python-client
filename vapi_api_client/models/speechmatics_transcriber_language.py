from enum import Enum


class SpeechmaticsTranscriberLanguage(str, Enum):
    AR = "ar"
    AUTO = "auto"
    BA = "ba"
    BE = "be"
    BG = "bg"
    BN = "bn"
    CA = "ca"
    CMN = "cmn"
    CS = "cs"
    CY = "cy"
    DA = "da"
    DE = "de"
    EL = "el"
    EN = "en"
    EO = "eo"
    ES = "es"
    ET = "et"
    EU = "eu"
    FA = "fa"
    FI = "fi"
    FR = "fr"
    GA = "ga"
    GL = "gl"
    HE = "he"
    HI = "hi"
    HR = "hr"
    HU = "hu"
    IA = "ia"
    ID = "id"
    IT = "it"
    JA = "ja"
    KO = "ko"
    LT = "lt"
    LV = "lv"
    MN = "mn"
    MR = "mr"
    MS = "ms"
    MT = "mt"
    NL = "nl"
    NO = "no"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SK = "sk"
    SL = "sl"
    SV = "sv"
    SW = "sw"
    TA = "ta"
    TH = "th"
    TR = "tr"
    UG = "ug"
    UK = "uk"
    UR = "ur"
    VI = "vi"
    YUE = "yue"

    def __str__(self) -> str:
        return str(self.value)

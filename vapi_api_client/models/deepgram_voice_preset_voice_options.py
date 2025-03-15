from enum import Enum


class DeepgramVoicePresetVoiceOptions(str, Enum):
    ANGUS = "angus"
    ARCAS = "arcas"
    ASTERIA = "asteria"
    ATHENA = "athena"
    HELIOS = "helios"
    HERA = "hera"
    LUNA = "luna"
    ORION = "orion"
    ORPHEUS = "orpheus"
    PERSEUS = "perseus"
    STELLA = "stella"
    ZEUS = "zeus"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class FallbackSmallestAIVoicePresetVoiceOptions(str, Enum):
    AARAV = "aarav"
    ANANYA = "ananya"
    ARAVIND = "aravind"
    ARMAN = "arman"
    DEEPIKA = "deepika"
    DIYA = "diya"
    EMILY = "emily"
    ISHA = "isha"
    JAMES = "james"
    JASMINE = "jasmine"
    KAJAL = "kajal"
    MANSI = "mansi"
    MITHALI = "mithali"
    MONIKA = "monika"
    NIHARIKA = "niharika"
    NISHA = "nisha"
    POOJA = "pooja"
    RADHIKA = "radhika"
    RAGHAV = "raghav"
    RAJ = "raj"
    RAMAN = "raman"
    SAINA = "saina"
    SANYA = "sanya"
    SAURABH = "saurabh"
    WILLIAM = "william"

    def __str__(self) -> str:
        return str(self.value)

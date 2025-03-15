from enum import Enum


class FallbackPlayHTVoicePresetVoiceOptions(str, Enum):
    CHRIS = "chris"
    DAVIS = "davis"
    DONNA = "donna"
    JACK = "jack"
    JENNIFER = "jennifer"
    MATT = "matt"
    MELISSA = "melissa"
    MICHAEL = "michael"
    RUBY = "ruby"
    WILL = "will"

    def __str__(self) -> str:
        return str(self.value)

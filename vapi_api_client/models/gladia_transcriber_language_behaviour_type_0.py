from enum import Enum


class GladiaTranscriberLanguageBehaviourType0(str, Enum):
    AUTOMATIC_MULTIPLE_LANGUAGES = "automatic multiple languages"
    AUTOMATIC_SINGLE_LANGUAGE = "automatic single language"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)

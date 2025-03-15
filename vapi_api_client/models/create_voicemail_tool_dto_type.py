from enum import Enum


class CreateVoicemailToolDTOType(str, Enum):
    VOICEMAIL = "voicemail"

    def __str__(self) -> str:
        return str(self.value)

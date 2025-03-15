from enum import Enum


class CreateSpeechmaticsCredentialDTOProvider(str, Enum):
    SPEECHMATICS = "speechmatics"

    def __str__(self) -> str:
        return str(self.value)

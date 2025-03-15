from enum import Enum


class AssemblyAITranscriberLanguage(str, Enum):
    EN = "en"

    def __str__(self) -> str:
        return str(self.value)

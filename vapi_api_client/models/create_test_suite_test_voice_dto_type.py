from enum import Enum


class CreateTestSuiteTestVoiceDtoType(str, Enum):
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class TestSuiteRunStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class FileStatus(str, Enum):
    DONE = "done"
    FAILED = "failed"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)

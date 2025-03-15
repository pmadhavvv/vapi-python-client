from enum import Enum


class HookOn(str, Enum):
    TASK_DELAYED = "task.delayed"
    TASK_OUTPUT_CONFIRMATION = "task.output.confirmation"
    TASK_START = "task.start"

    def __str__(self) -> str:
        return str(self.value)

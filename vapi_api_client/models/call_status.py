from enum import Enum


class CallStatus(str, Enum):
    ENDED = "ended"
    FORWARDING = "forwarding"
    IN_PROGRESS = "in-progress"
    QUEUED = "queued"
    RINGING = "ringing"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)

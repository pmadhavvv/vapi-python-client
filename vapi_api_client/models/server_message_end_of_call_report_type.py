from enum import Enum


class ServerMessageEndOfCallReportType(str, Enum):
    END_OF_CALL_REPORT = "end-of-call-report"

    def __str__(self) -> str:
        return str(self.value)

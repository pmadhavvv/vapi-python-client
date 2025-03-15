from enum import Enum


class LoggingControllerLogsQueryType(str, Enum):
    API = "API"
    CALL = "Call"
    PROVIDER = "Provider"
    WEBHOOK = "Webhook"

    def __str__(self) -> str:
        return str(self.value)

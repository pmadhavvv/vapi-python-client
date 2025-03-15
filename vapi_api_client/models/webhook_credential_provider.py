from enum import Enum


class WebhookCredentialProvider(str, Enum):
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)

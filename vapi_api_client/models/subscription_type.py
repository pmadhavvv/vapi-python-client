from enum import Enum


class SubscriptionType(str, Enum):
    ENTERPRISE = "enterprise"
    PAY_AS_YOU_GO = "pay-as-you-go"
    TRIAL = "trial"

    def __str__(self) -> str:
        return str(self.value)

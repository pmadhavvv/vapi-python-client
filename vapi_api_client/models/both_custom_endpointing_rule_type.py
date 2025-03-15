from enum import Enum


class BothCustomEndpointingRuleType(str, Enum):
    BOTH = "both"

    def __str__(self) -> str:
        return str(self.value)

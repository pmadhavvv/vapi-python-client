from enum import Enum


class StartSpeakingPlanSmartEndpointingEnabledType1(str, Enum):
    LIVEKIT = "livekit"

    def __str__(self) -> str:
        return str(self.value)

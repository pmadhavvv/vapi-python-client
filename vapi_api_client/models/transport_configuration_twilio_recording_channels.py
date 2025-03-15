from enum import Enum


class TransportConfigurationTwilioRecordingChannels(str, Enum):
    DUAL = "dual"
    MONO = "mono"

    def __str__(self) -> str:
        return str(self.value)

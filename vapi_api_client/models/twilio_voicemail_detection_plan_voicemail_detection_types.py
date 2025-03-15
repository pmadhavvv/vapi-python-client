from enum import Enum


class TwilioVoicemailDetectionPlanVoicemailDetectionTypes(str, Enum):
    FAX = "fax"
    HUMAN = "human"
    MACHINE_END_BEEP = "machine_end_beep"
    MACHINE_END_OTHER = "machine_end_other"
    MACHINE_END_SILENCE = "machine_end_silence"
    MACHINE_START = "machine_start"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)

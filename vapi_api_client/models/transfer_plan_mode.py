from enum import Enum


class TransferPlanMode(str, Enum):
    BLIND_TRANSFER = "blind-transfer"
    BLIND_TRANSFER_ADD_SUMMARY_TO_SIP_HEADER = "blind-transfer-add-summary-to-sip-header"
    WARM_TRANSFER_SAY_MESSAGE = "warm-transfer-say-message"
    WARM_TRANSFER_SAY_SUMMARY = "warm-transfer-say-summary"
    WARM_TRANSFER_TWIML = "warm-transfer-twiml"
    WARM_TRANSFER_WAIT_FOR_OPERATOR_TO_SPEAK_FIRST_AND_THEN_SAY_MESSAGE = (
        "warm-transfer-wait-for-operator-to-speak-first-and-then-say-message"
    )
    WARM_TRANSFER_WAIT_FOR_OPERATOR_TO_SPEAK_FIRST_AND_THEN_SAY_SUMMARY = (
        "warm-transfer-wait-for-operator-to-speak-first-and-then-say-summary"
    )

    def __str__(self) -> str:
        return str(self.value)

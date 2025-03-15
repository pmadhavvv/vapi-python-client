from enum import Enum


class TransferDestinationAssistantTransferMode(str, Enum):
    DELETE_HISTORY = "delete-history"
    ROLLING_HISTORY = "rolling-history"
    SWAP_SYSTEM_MESSAGE_IN_HISTORY = "swap-system-message-in-history"
    SWAP_SYSTEM_MESSAGE_IN_HISTORY_AND_REMOVE_TRANSFER_TOOL_MESSAGES = (
        "swap-system-message-in-history-and-remove-transfer-tool-messages"
    )

    def __str__(self) -> str:
        return str(self.value)

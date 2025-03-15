from enum import Enum


class TextEditorToolWithToolCallType(str, Enum):
    TEXTEDITOR = "textEditor"

    def __str__(self) -> str:
        return str(self.value)

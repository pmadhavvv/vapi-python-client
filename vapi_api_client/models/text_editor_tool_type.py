from enum import Enum


class TextEditorToolType(str, Enum):
    TEXTEDITOR = "textEditor"

    def __str__(self) -> str:
        return str(self.value)

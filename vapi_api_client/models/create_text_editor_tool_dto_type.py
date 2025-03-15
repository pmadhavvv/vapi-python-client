from enum import Enum


class CreateTextEditorToolDTOType(str, Enum):
    TEXTEDITOR = "textEditor"

    def __str__(self) -> str:
        return str(self.value)

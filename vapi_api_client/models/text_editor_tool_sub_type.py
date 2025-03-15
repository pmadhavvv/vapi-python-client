from enum import Enum


class TextEditorToolSubType(str, Enum):
    TEXT_EDITOR_20241022 = "text_editor_20241022"

    def __str__(self) -> str:
        return str(self.value)

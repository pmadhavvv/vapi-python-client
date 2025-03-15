from enum import Enum


class TextEditorToolName(str, Enum):
    STR_REPLACE_EDITOR = "str_replace_editor"

    def __str__(self) -> str:
        return str(self.value)

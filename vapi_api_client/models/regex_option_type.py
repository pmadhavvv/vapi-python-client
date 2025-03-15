from enum import Enum


class RegexOptionType(str, Enum):
    IGNORE_CASE = "ignore-case"
    MULTI_LINE = "multi-line"
    WHOLE_WORD = "whole-word"

    def __str__(self) -> str:
        return str(self.value)

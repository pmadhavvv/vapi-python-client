from enum import Enum


class ChunkPlanPunctuationBoundaries(str, Enum):
    VALUE_0 = "。"
    VALUE_1 = "，"
    VALUE_10 = "॥"
    VALUE_11 = "|"
    VALUE_12 = "||"
    VALUE_13 = ","
    VALUE_14 = ":"
    VALUE_2 = "."
    VALUE_3 = "!"
    VALUE_4 = "?"
    VALUE_5 = ";"
    VALUE_6 = ")"
    VALUE_7 = "،"
    VALUE_8 = "۔"
    VALUE_9 = "।"

    def __str__(self) -> str:
        return str(self.value)

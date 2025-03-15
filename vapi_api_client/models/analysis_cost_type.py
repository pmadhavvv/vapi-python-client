from enum import Enum


class AnalysisCostType(str, Enum):
    ANALYSIS = "analysis"

    def __str__(self) -> str:
        return str(self.value)

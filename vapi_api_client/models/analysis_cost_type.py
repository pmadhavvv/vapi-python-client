from enum import Enum


class AnalysisCostType(str, Enum):
    ANALYSIS = "analysis"
    KNOWLEDGE_BASE = "knowledge-base"

    def __str__(self) -> str:
        return str(self.value)

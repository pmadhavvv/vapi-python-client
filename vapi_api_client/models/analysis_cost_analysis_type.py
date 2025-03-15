from enum import Enum


class AnalysisCostAnalysisType(str, Enum):
    STRUCTUREDDATA = "structuredData"
    SUCCESSEVALUATION = "successEvaluation"
    SUMMARY = "summary"

    def __str__(self) -> str:
        return str(self.value)

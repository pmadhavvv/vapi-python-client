from enum import Enum


class AnalyticsQueryGroupBy(str, Enum):
    ANALYSIS_SUCCESSEVALUATION = "analysis.successEvaluation"
    ASSISTANTID = "assistantId"
    ENDEDREASON = "endedReason"
    STATUS = "status"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)

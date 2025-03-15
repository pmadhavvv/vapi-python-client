from enum import Enum


class SuccessEvaluationPlanRubric(str, Enum):
    AUTOMATICRUBRIC = "AutomaticRubric"
    CHECKLIST = "Checklist"
    DESCRIPTIVESCALE = "DescriptiveScale"
    LIKERTSCALE = "LikertScale"
    MATRIX = "Matrix"
    NUMERICSCALE = "NumericScale"
    PASSFAIL = "PassFail"
    PERCENTAGESCALE = "PercentageScale"

    def __str__(self) -> str:
        return str(self.value)

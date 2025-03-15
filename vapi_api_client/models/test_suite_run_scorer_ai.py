from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_suite_run_scorer_ai_result import TestSuiteRunScorerAIResult
from ..models.test_suite_run_scorer_ai_type import TestSuiteRunScorerAIType

T = TypeVar("T", bound="TestSuiteRunScorerAI")


@_attrs_define
class TestSuiteRunScorerAI:
    """
    Attributes:
        type_ (TestSuiteRunScorerAIType): This is the type of the scorer, which must be AI.
        result (TestSuiteRunScorerAIResult): This is the result of the test suite.
        reasoning (str): This is the reasoning provided by the AI scorer.
        rubric (str): This is the rubric used by the AI scorer.
    """

    type_: TestSuiteRunScorerAIType
    result: TestSuiteRunScorerAIResult
    reasoning: str
    rubric: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        result = self.result.value

        reasoning = self.reasoning

        rubric = self.rubric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "result": result,
                "reasoning": reasoning,
                "rubric": rubric,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = TestSuiteRunScorerAIType(d.pop("type"))

        result = TestSuiteRunScorerAIResult(d.pop("result"))

        reasoning = d.pop("reasoning")

        rubric = d.pop("rubric")

        test_suite_run_scorer_ai = cls(
            type_=type_,
            result=result,
            reasoning=reasoning,
            rubric=rubric,
        )

        test_suite_run_scorer_ai.additional_properties = d
        return test_suite_run_scorer_ai

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

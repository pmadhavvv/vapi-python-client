from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_suite_test_scorer_ai_type import TestSuiteTestScorerAIType

T = TypeVar("T", bound="TestSuiteTestScorerAI")


@_attrs_define
class TestSuiteTestScorerAI:
    """
    Attributes:
        type_ (TestSuiteTestScorerAIType): This is the type of the scorer, which must be AI.
        rubric (str): This is the rubric used by the AI scorer.
    """

    type_: TestSuiteTestScorerAIType
    rubric: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        rubric = self.rubric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "rubric": rubric,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = TestSuiteTestScorerAIType(d.pop("type"))

        rubric = d.pop("rubric")

        test_suite_test_scorer_ai = cls(
            type_=type_,
            rubric=rubric,
        )

        test_suite_test_scorer_ai.additional_properties = d
        return test_suite_test_scorer_ai

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

from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.test_suite_run_scorer_ai import TestSuiteRunScorerAI
    from ..models.test_suite_run_test_attempt_call import TestSuiteRunTestAttemptCall


T = TypeVar("T", bound="TestSuiteRunTestAttempt")


@_attrs_define
class TestSuiteRunTestAttempt:
    """
    Attributes:
        scorer_results (list['TestSuiteRunScorerAI']): These are the results of the scorers used to evaluate the test
            attempt.
        call (TestSuiteRunTestAttemptCall):
    """

    scorer_results: list["TestSuiteRunScorerAI"]
    call: "TestSuiteRunTestAttemptCall"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scorer_results = []
        for scorer_results_item_data in self.scorer_results:
            scorer_results_item = scorer_results_item_data.to_dict()
            scorer_results.append(scorer_results_item)

        call = self.call.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scorerResults": scorer_results,
                "call": call,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.test_suite_run_scorer_ai import TestSuiteRunScorerAI
        from ..models.test_suite_run_test_attempt_call import TestSuiteRunTestAttemptCall

        d = src_dict.copy()
        scorer_results = []
        _scorer_results = d.pop("scorerResults")
        for scorer_results_item_data in _scorer_results:
            scorer_results_item = TestSuiteRunScorerAI.from_dict(scorer_results_item_data)

            scorer_results.append(scorer_results_item)

        call = TestSuiteRunTestAttemptCall.from_dict(d.pop("call"))

        test_suite_run_test_attempt = cls(
            scorer_results=scorer_results,
            call=call,
        )

        test_suite_run_test_attempt.additional_properties = d
        return test_suite_run_test_attempt

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.test_suite_run_test_attempt import TestSuiteRunTestAttempt
    from ..models.test_suite_test_voice import TestSuiteTestVoice


T = TypeVar("T", bound="TestSuiteRunTestResult")


@_attrs_define
class TestSuiteRunTestResult:
    """
    Attributes:
        test ('TestSuiteTestVoice'): This is the test that was run.
        attempts (list['TestSuiteRunTestAttempt']): These are the attempts made for this test.
    """

    test: "TestSuiteTestVoice"
    attempts: list["TestSuiteRunTestAttempt"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_suite_test_voice import TestSuiteTestVoice

        test: dict[str, Any]
        if isinstance(self.test, TestSuiteTestVoice):
            test = self.test.to_dict()

        attempts = []
        for attempts_item_data in self.attempts:
            attempts_item = attempts_item_data.to_dict()
            attempts.append(attempts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test": test,
                "attempts": attempts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_suite_run_test_attempt import TestSuiteRunTestAttempt
        from ..models.test_suite_test_voice import TestSuiteTestVoice

        d = dict(src_dict)

        def _parse_test(data: object) -> "TestSuiteTestVoice":
            if not isinstance(data, dict):
                raise TypeError()
            test_type_0 = TestSuiteTestVoice.from_dict(data)

            return test_type_0

        test = _parse_test(d.pop("test"))

        attempts = []
        _attempts = d.pop("attempts")
        for attempts_item_data in _attempts:
            attempts_item = TestSuiteRunTestAttempt.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        test_suite_run_test_result = cls(
            test=test,
            attempts=attempts,
        )

        test_suite_run_test_result.additional_properties = d
        return test_suite_run_test_result

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

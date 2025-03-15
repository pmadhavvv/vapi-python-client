from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.artifact import Artifact


T = TypeVar("T", bound="TestSuiteRunTestAttemptCall")


@_attrs_define
class TestSuiteRunTestAttemptCall:
    """
    Attributes:
        artifact (Artifact):
    """

    artifact: "Artifact"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact = self.artifact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artifact": artifact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.artifact import Artifact

        d = src_dict.copy()
        artifact = Artifact.from_dict(d.pop("artifact"))

        test_suite_run_test_attempt_call = cls(
            artifact=artifact,
        )

        test_suite_run_test_attempt_call.additional_properties = d
        return test_suite_run_test_attempt_call

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

from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTestSuiteDto")


@_attrs_define
class CreateTestSuiteDto:
    """
    Attributes:
        name (Union[Unset, str]): This is the name of the test suite.
        phone_number_id (Union[Unset, str]): This is the phone number ID associated with this test suite.
    """

    name: Union[Unset, str] = UNSET
    phone_number_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        phone_number_id = self.phone_number_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if phone_number_id is not UNSET:
            field_dict["phoneNumberId"] = phone_number_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        phone_number_id = d.pop("phoneNumberId", UNSET)

        create_test_suite_dto = cls(
            name=name,
            phone_number_id=phone_number_id,
        )

        create_test_suite_dto.additional_properties = d
        return create_test_suite_dto

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

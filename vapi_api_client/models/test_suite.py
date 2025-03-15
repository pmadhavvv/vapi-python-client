import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestSuite")


@_attrs_define
class TestSuite:
    """
    Attributes:
        id (str): This is the unique identifier for the test suite.
        org_id (str): This is the unique identifier for the org that this test suite belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the test suite was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the test suite was last updated.
        name (Union[Unset, str]): This is the name of the test suite.
        phone_number_id (Union[Unset, str]): This is the phone number ID associated with this test suite.
    """

    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Union[Unset, str] = UNSET
    phone_number_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        phone_number_id = self.phone_number_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if phone_number_id is not UNSET:
            field_dict["phoneNumberId"] = phone_number_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        name = d.pop("name", UNSET)

        phone_number_id = d.pop("phoneNumberId", UNSET)

        test_suite = cls(
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            phone_number_id=phone_number_id,
        )

        test_suite.additional_properties = d
        return test_suite

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

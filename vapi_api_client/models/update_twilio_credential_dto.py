from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTwilioCredentialDTO")


@_attrs_define
class UpdateTwilioCredentialDTO:
    """
    Attributes:
        auth_token (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        account_sid (Union[Unset, str]):
    """

    auth_token: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    account_sid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_token = self.auth_token

        name = self.name

        account_sid = self.account_sid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token
        if name is not UNSET:
            field_dict["name"] = name
        if account_sid is not UNSET:
            field_dict["accountSid"] = account_sid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        auth_token = d.pop("authToken", UNSET)

        name = d.pop("name", UNSET)

        account_sid = d.pop("accountSid", UNSET)

        update_twilio_credential_dto = cls(
            auth_token=auth_token,
            name=name,
            account_sid=account_sid,
        )

        update_twilio_credential_dto.additional_properties = d
        return update_twilio_credential_dto

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

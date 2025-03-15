from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_twilio_credential_dto_provider import CreateTwilioCredentialDTOProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTwilioCredentialDTO")


@_attrs_define
class CreateTwilioCredentialDTO:
    """
    Attributes:
        provider (CreateTwilioCredentialDTOProvider):
        auth_token (str): This is not returned in the API.
        account_sid (str):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateTwilioCredentialDTOProvider
    auth_token: str
    account_sid: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        auth_token = self.auth_token

        account_sid = self.account_sid

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "authToken": auth_token,
                "accountSid": account_sid,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = CreateTwilioCredentialDTOProvider(d.pop("provider"))

        auth_token = d.pop("authToken")

        account_sid = d.pop("accountSid")

        name = d.pop("name", UNSET)

        create_twilio_credential_dto = cls(
            provider=provider,
            auth_token=auth_token,
            account_sid=account_sid,
            name=name,
        )

        create_twilio_credential_dto.additional_properties = d
        return create_twilio_credential_dto

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

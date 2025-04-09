import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.twilio_credential_provider import TwilioCredentialProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="TwilioCredential")


@_attrs_define
class TwilioCredential:
    """
    Attributes:
        provider (TwilioCredentialProvider):
        auth_token (str): This is not returned in the API.
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        account_sid (str):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: TwilioCredentialProvider
    auth_token: str
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    account_sid: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        auth_token = self.auth_token

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        account_sid = self.account_sid

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "authToken": auth_token,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "accountSid": account_sid,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = TwilioCredentialProvider(d.pop("provider"))

        auth_token = d.pop("authToken")

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        account_sid = d.pop("accountSid")

        name = d.pop("name", UNSET)

        twilio_credential = cls(
            provider=provider,
            auth_token=auth_token,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            account_sid=account_sid,
            name=name,
        )

        twilio_credential.additional_properties = d
        return twilio_credential

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

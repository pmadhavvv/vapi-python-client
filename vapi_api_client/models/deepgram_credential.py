import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deepgram_credential_provider import DeepgramCredentialProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepgramCredential")


@_attrs_define
class DeepgramCredential:
    """
    Attributes:
        provider (DeepgramCredentialProvider):
        api_key (str): This is not returned in the API.
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        api_url (Union[Unset, str]): This can be used to point to an onprem Deepgram instance. Defaults to
            api.deepgram.com.
    """

    provider: DeepgramCredentialProvider
    api_key: str
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Union[Unset, str] = UNSET
    api_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        api_key = self.api_key

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        api_url = self.api_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "apiKey": api_key,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = DeepgramCredentialProvider(d.pop("provider"))

        api_key = d.pop("apiKey")

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        name = d.pop("name", UNSET)

        api_url = d.pop("apiUrl", UNSET)

        deepgram_credential = cls(
            provider=provider,
            api_key=api_key,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            api_url=api_url,
        )

        deepgram_credential.additional_properties = d
        return deepgram_credential

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

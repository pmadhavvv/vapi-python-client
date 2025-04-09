import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.langfuse_credential_provider import LangfuseCredentialProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="LangfuseCredential")


@_attrs_define
class LangfuseCredential:
    """
    Attributes:
        provider (LangfuseCredentialProvider):
        public_key (str): The public key for Langfuse project. Eg: pk-lf-...
        api_key (str): The secret key for Langfuse project. Eg: sk-lf-... .This is not returned in the API.
        api_url (str): The host URL for Langfuse project. Eg: https://cloud.langfuse.com
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: LangfuseCredentialProvider
    public_key: str
    api_key: str
    api_url: str
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        public_key = self.public_key

        api_key = self.api_key

        api_url = self.api_url

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "publicKey": public_key,
                "apiKey": api_key,
                "apiUrl": api_url,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = LangfuseCredentialProvider(d.pop("provider"))

        public_key = d.pop("publicKey")

        api_key = d.pop("apiKey")

        api_url = d.pop("apiUrl")

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        name = d.pop("name", UNSET)

        langfuse_credential = cls(
            provider=provider,
            public_key=public_key,
            api_key=api_key,
            api_url=api_url,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
        )

        langfuse_credential.additional_properties = d
        return langfuse_credential

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

import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vonage_credential_provider import VonageCredentialProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="VonageCredential")


@_attrs_define
class VonageCredential:
    """
    Attributes:
        vonage_application_private_key (str): This is not returned in the API.
        provider (VonageCredentialProvider):
        api_secret (str): This is not returned in the API.
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        vonage_application_id (str): This is the Vonage Application ID for the credential.

            Only relevant for Vonage credentials.
        api_key (str):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    vonage_application_private_key: str
    provider: VonageCredentialProvider
    api_secret: str
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    vonage_application_id: str
    api_key: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vonage_application_private_key = self.vonage_application_private_key

        provider = self.provider.value

        api_secret = self.api_secret

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        vonage_application_id = self.vonage_application_id

        api_key = self.api_key

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vonageApplicationPrivateKey": vonage_application_private_key,
                "provider": provider,
                "apiSecret": api_secret,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "vonageApplicationId": vonage_application_id,
                "apiKey": api_key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        vonage_application_private_key = d.pop("vonageApplicationPrivateKey")

        provider = VonageCredentialProvider(d.pop("provider"))

        api_secret = d.pop("apiSecret")

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        vonage_application_id = d.pop("vonageApplicationId")

        api_key = d.pop("apiKey")

        name = d.pop("name", UNSET)

        vonage_credential = cls(
            vonage_application_private_key=vonage_application_private_key,
            provider=provider,
            api_secret=api_secret,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            vonage_application_id=vonage_application_id,
            api_key=api_key,
            name=name,
        )

        vonage_credential.additional_properties = d
        return vonage_credential

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

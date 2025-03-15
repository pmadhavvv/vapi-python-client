import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.azure_open_ai_credential_models import AzureOpenAICredentialModels
from ..models.azure_open_ai_credential_provider import AzureOpenAICredentialProvider
from ..models.azure_open_ai_credential_region import AzureOpenAICredentialRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureOpenAICredential")


@_attrs_define
class AzureOpenAICredential:
    """
    Attributes:
        provider (AzureOpenAICredentialProvider):
        region (AzureOpenAICredentialRegion):
        models (AzureOpenAICredentialModels):  Example: ['gpt-4-0125-preview', 'gpt-4-0613'].
        open_ai_key (str): This is not returned in the API.
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        open_ai_endpoint (str):
        ocp_apim_subscription_key (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: AzureOpenAICredentialProvider
    region: AzureOpenAICredentialRegion
    models: AzureOpenAICredentialModels
    open_ai_key: str
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    open_ai_endpoint: str
    ocp_apim_subscription_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        region = self.region.value

        models = self.models.value

        open_ai_key = self.open_ai_key

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        open_ai_endpoint = self.open_ai_endpoint

        ocp_apim_subscription_key = self.ocp_apim_subscription_key

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "region": region,
                "models": models,
                "openAIKey": open_ai_key,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "openAIEndpoint": open_ai_endpoint,
            }
        )
        if ocp_apim_subscription_key is not UNSET:
            field_dict["ocpApimSubscriptionKey"] = ocp_apim_subscription_key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = AzureOpenAICredentialProvider(d.pop("provider"))

        region = AzureOpenAICredentialRegion(d.pop("region"))

        models = AzureOpenAICredentialModels(d.pop("models"))

        open_ai_key = d.pop("openAIKey")

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        open_ai_endpoint = d.pop("openAIEndpoint")

        ocp_apim_subscription_key = d.pop("ocpApimSubscriptionKey", UNSET)

        name = d.pop("name", UNSET)

        azure_open_ai_credential = cls(
            provider=provider,
            region=region,
            models=models,
            open_ai_key=open_ai_key,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            open_ai_endpoint=open_ai_endpoint,
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            name=name,
        )

        azure_open_ai_credential.additional_properties = d
        return azure_open_ai_credential

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

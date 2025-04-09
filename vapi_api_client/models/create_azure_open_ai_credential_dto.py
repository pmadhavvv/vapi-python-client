from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_azure_open_ai_credential_dto_models_item import CreateAzureOpenAICredentialDTOModelsItem
from ..models.create_azure_open_ai_credential_dto_provider import CreateAzureOpenAICredentialDTOProvider
from ..models.create_azure_open_ai_credential_dto_region import CreateAzureOpenAICredentialDTORegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAzureOpenAICredentialDTO")


@_attrs_define
class CreateAzureOpenAICredentialDTO:
    """
    Attributes:
        provider (CreateAzureOpenAICredentialDTOProvider):
        region (CreateAzureOpenAICredentialDTORegion):
        models (list[CreateAzureOpenAICredentialDTOModelsItem]):  Example: ['gpt-4-0125-preview', 'gpt-4-0613'].
        open_ai_key (str): This is not returned in the API.
        open_ai_endpoint (str):
        ocp_apim_subscription_key (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateAzureOpenAICredentialDTOProvider
    region: CreateAzureOpenAICredentialDTORegion
    models: list[CreateAzureOpenAICredentialDTOModelsItem]
    open_ai_key: str
    open_ai_endpoint: str
    ocp_apim_subscription_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        region = self.region.value

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.value
            models.append(models_item)

        open_ai_key = self.open_ai_key

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
                "openAIEndpoint": open_ai_endpoint,
            }
        )
        if ocp_apim_subscription_key is not UNSET:
            field_dict["ocpApimSubscriptionKey"] = ocp_apim_subscription_key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = CreateAzureOpenAICredentialDTOProvider(d.pop("provider"))

        region = CreateAzureOpenAICredentialDTORegion(d.pop("region"))

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = CreateAzureOpenAICredentialDTOModelsItem(models_item_data)

            models.append(models_item)

        open_ai_key = d.pop("openAIKey")

        open_ai_endpoint = d.pop("openAIEndpoint")

        ocp_apim_subscription_key = d.pop("ocpApimSubscriptionKey", UNSET)

        name = d.pop("name", UNSET)

        create_azure_open_ai_credential_dto = cls(
            provider=provider,
            region=region,
            models=models,
            open_ai_key=open_ai_key,
            open_ai_endpoint=open_ai_endpoint,
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            name=name,
        )

        create_azure_open_ai_credential_dto.additional_properties = d
        return create_azure_open_ai_credential_dto

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

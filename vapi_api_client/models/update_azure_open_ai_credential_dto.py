from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_azure_open_ai_credential_dto_models import UpdateAzureOpenAICredentialDTOModels
from ..models.update_azure_open_ai_credential_dto_region import UpdateAzureOpenAICredentialDTORegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAzureOpenAICredentialDTO")


@_attrs_define
class UpdateAzureOpenAICredentialDTO:
    """
    Attributes:
        region (Union[Unset, UpdateAzureOpenAICredentialDTORegion]):
        models (Union[Unset, UpdateAzureOpenAICredentialDTOModels]):  Example: ['gpt-4-0125-preview', 'gpt-4-0613'].
        open_ai_key (Union[Unset, str]): This is not returned in the API.
        ocp_apim_subscription_key (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        open_ai_endpoint (Union[Unset, str]):
    """

    region: Union[Unset, UpdateAzureOpenAICredentialDTORegion] = UNSET
    models: Union[Unset, UpdateAzureOpenAICredentialDTOModels] = UNSET
    open_ai_key: Union[Unset, str] = UNSET
    ocp_apim_subscription_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    open_ai_endpoint: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        models: Union[Unset, str] = UNSET
        if not isinstance(self.models, Unset):
            models = self.models.value

        open_ai_key = self.open_ai_key

        ocp_apim_subscription_key = self.ocp_apim_subscription_key

        name = self.name

        open_ai_endpoint = self.open_ai_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if models is not UNSET:
            field_dict["models"] = models
        if open_ai_key is not UNSET:
            field_dict["openAIKey"] = open_ai_key
        if ocp_apim_subscription_key is not UNSET:
            field_dict["ocpApimSubscriptionKey"] = ocp_apim_subscription_key
        if name is not UNSET:
            field_dict["name"] = name
        if open_ai_endpoint is not UNSET:
            field_dict["openAIEndpoint"] = open_ai_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _region = d.pop("region", UNSET)
        region: Union[Unset, UpdateAzureOpenAICredentialDTORegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = UpdateAzureOpenAICredentialDTORegion(_region)

        _models = d.pop("models", UNSET)
        models: Union[Unset, UpdateAzureOpenAICredentialDTOModels]
        if isinstance(_models, Unset):
            models = UNSET
        else:
            models = UpdateAzureOpenAICredentialDTOModels(_models)

        open_ai_key = d.pop("openAIKey", UNSET)

        ocp_apim_subscription_key = d.pop("ocpApimSubscriptionKey", UNSET)

        name = d.pop("name", UNSET)

        open_ai_endpoint = d.pop("openAIEndpoint", UNSET)

        update_azure_open_ai_credential_dto = cls(
            region=region,
            models=models,
            open_ai_key=open_ai_key,
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            name=name,
            open_ai_endpoint=open_ai_endpoint,
        )

        update_azure_open_ai_credential_dto.additional_properties = d
        return update_azure_open_ai_credential_dto

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

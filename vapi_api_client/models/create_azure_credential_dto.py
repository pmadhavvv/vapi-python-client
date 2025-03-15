from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_azure_credential_dto_provider import CreateAzureCredentialDTOProvider
from ..models.create_azure_credential_dto_region import CreateAzureCredentialDTORegion
from ..models.create_azure_credential_dto_service import CreateAzureCredentialDTOService
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_blob_storage_bucket_plan import AzureBlobStorageBucketPlan


T = TypeVar("T", bound="CreateAzureCredentialDTO")


@_attrs_define
class CreateAzureCredentialDTO:
    """
    Attributes:
        provider (CreateAzureCredentialDTOProvider):
        service (CreateAzureCredentialDTOService): This is the service being used in Azure.
        region (Union[Unset, CreateAzureCredentialDTORegion]): This is the region of the Azure resource.
        api_key (Union[Unset, str]): This is not returned in the API.
        bucket_plan (Union[Unset, AzureBlobStorageBucketPlan]):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateAzureCredentialDTOProvider
    service: CreateAzureCredentialDTOService
    region: Union[Unset, CreateAzureCredentialDTORegion] = UNSET
    api_key: Union[Unset, str] = UNSET
    bucket_plan: Union[Unset, "AzureBlobStorageBucketPlan"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        service = self.service.value

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        api_key = self.api_key

        bucket_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_plan, Unset):
            bucket_plan = self.bucket_plan.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "service": service,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if bucket_plan is not UNSET:
            field_dict["bucketPlan"] = bucket_plan
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.azure_blob_storage_bucket_plan import AzureBlobStorageBucketPlan

        d = src_dict.copy()
        provider = CreateAzureCredentialDTOProvider(d.pop("provider"))

        service = CreateAzureCredentialDTOService(d.pop("service"))

        _region = d.pop("region", UNSET)
        region: Union[Unset, CreateAzureCredentialDTORegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = CreateAzureCredentialDTORegion(_region)

        api_key = d.pop("apiKey", UNSET)

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, AzureBlobStorageBucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = AzureBlobStorageBucketPlan.from_dict(_bucket_plan)

        name = d.pop("name", UNSET)

        create_azure_credential_dto = cls(
            provider=provider,
            service=service,
            region=region,
            api_key=api_key,
            bucket_plan=bucket_plan,
            name=name,
        )

        create_azure_credential_dto.additional_properties = d
        return create_azure_credential_dto

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

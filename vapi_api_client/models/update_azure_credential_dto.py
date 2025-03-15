from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_azure_credential_dto_region import UpdateAzureCredentialDTORegion
from ..models.update_azure_credential_dto_service import UpdateAzureCredentialDTOService
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_blob_storage_bucket_plan import AzureBlobStorageBucketPlan


T = TypeVar("T", bound="UpdateAzureCredentialDTO")


@_attrs_define
class UpdateAzureCredentialDTO:
    """
    Attributes:
        service (Union[Unset, UpdateAzureCredentialDTOService]): This is the service being used in Azure.
        region (Union[Unset, UpdateAzureCredentialDTORegion]): This is the region of the Azure resource.
        api_key (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        bucket_plan (Union[Unset, AzureBlobStorageBucketPlan]):
    """

    service: Union[Unset, UpdateAzureCredentialDTOService] = UNSET
    region: Union[Unset, UpdateAzureCredentialDTORegion] = UNSET
    api_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    bucket_plan: Union[Unset, "AzureBlobStorageBucketPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service: Union[Unset, str] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.value

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        api_key = self.api_key

        name = self.name

        bucket_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_plan, Unset):
            bucket_plan = self.bucket_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if region is not UNSET:
            field_dict["region"] = region
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if name is not UNSET:
            field_dict["name"] = name
        if bucket_plan is not UNSET:
            field_dict["bucketPlan"] = bucket_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.azure_blob_storage_bucket_plan import AzureBlobStorageBucketPlan

        d = src_dict.copy()
        _service = d.pop("service", UNSET)
        service: Union[Unset, UpdateAzureCredentialDTOService]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = UpdateAzureCredentialDTOService(_service)

        _region = d.pop("region", UNSET)
        region: Union[Unset, UpdateAzureCredentialDTORegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = UpdateAzureCredentialDTORegion(_region)

        api_key = d.pop("apiKey", UNSET)

        name = d.pop("name", UNSET)

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, AzureBlobStorageBucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = AzureBlobStorageBucketPlan.from_dict(_bucket_plan)

        update_azure_credential_dto = cls(
            service=service,
            region=region,
            api_key=api_key,
            name=name,
            bucket_plan=bucket_plan,
        )

        update_azure_credential_dto.additional_properties = d
        return update_azure_credential_dto

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

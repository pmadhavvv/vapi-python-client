import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.azure_credential_provider import AzureCredentialProvider
from ..models.azure_credential_region import AzureCredentialRegion
from ..models.azure_credential_service import AzureCredentialService
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_blob_storage_bucket_plan import AzureBlobStorageBucketPlan


T = TypeVar("T", bound="AzureCredential")


@_attrs_define
class AzureCredential:
    """
    Attributes:
        provider (AzureCredentialProvider):
        service (AzureCredentialService): This is the service being used in Azure.
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        region (Union[Unset, AzureCredentialRegion]): This is the region of the Azure resource.
        api_key (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        bucket_plan (Union[Unset, AzureBlobStorageBucketPlan]):
    """

    provider: AzureCredentialProvider
    service: AzureCredentialService
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    region: Union[Unset, AzureCredentialRegion] = UNSET
    api_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    bucket_plan: Union[Unset, "AzureBlobStorageBucketPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        service = self.service.value

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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
        field_dict.update(
            {
                "provider": provider,
                "service": service,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
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
        provider = AzureCredentialProvider(d.pop("provider"))

        service = AzureCredentialService(d.pop("service"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _region = d.pop("region", UNSET)
        region: Union[Unset, AzureCredentialRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = AzureCredentialRegion(_region)

        api_key = d.pop("apiKey", UNSET)

        name = d.pop("name", UNSET)

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, AzureBlobStorageBucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = AzureBlobStorageBucketPlan.from_dict(_bucket_plan)

        azure_credential = cls(
            provider=provider,
            service=service,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            region=region,
            api_key=api_key,
            name=name,
            bucket_plan=bucket_plan,
        )

        azure_credential.additional_properties = d
        return azure_credential

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

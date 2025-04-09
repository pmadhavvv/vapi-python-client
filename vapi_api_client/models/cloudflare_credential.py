import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cloudflare_credential_provider import CloudflareCredentialProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloudflare_r2_bucket_plan import CloudflareR2BucketPlan


T = TypeVar("T", bound="CloudflareCredential")


@_attrs_define
class CloudflareCredential:
    """
    Attributes:
        provider (CloudflareCredentialProvider): Credential provider. Only allowed value is cloudflare
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        account_id (Union[Unset, str]): Cloudflare Account Id.
        api_key (Union[Unset, str]): Cloudflare API Key / Token.
        account_email (Union[Unset, str]): Cloudflare Account Email.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        bucket_plan (Union[Unset, CloudflareR2BucketPlan]):
    """

    provider: CloudflareCredentialProvider
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    account_id: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    account_email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    bucket_plan: Union[Unset, "CloudflareR2BucketPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        account_id = self.account_id

        api_key = self.api_key

        account_email = self.account_email

        name = self.name

        bucket_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_plan, Unset):
            bucket_plan = self.bucket_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if account_email is not UNSET:
            field_dict["accountEmail"] = account_email
        if name is not UNSET:
            field_dict["name"] = name
        if bucket_plan is not UNSET:
            field_dict["bucketPlan"] = bucket_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloudflare_r2_bucket_plan import CloudflareR2BucketPlan

        d = dict(src_dict)
        provider = CloudflareCredentialProvider(d.pop("provider"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        account_id = d.pop("accountId", UNSET)

        api_key = d.pop("apiKey", UNSET)

        account_email = d.pop("accountEmail", UNSET)

        name = d.pop("name", UNSET)

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, CloudflareR2BucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = CloudflareR2BucketPlan.from_dict(_bucket_plan)

        cloudflare_credential = cls(
            provider=provider,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            account_id=account_id,
            api_key=api_key,
            account_email=account_email,
            name=name,
            bucket_plan=bucket_plan,
        )

        cloudflare_credential.additional_properties = d
        return cloudflare_credential

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

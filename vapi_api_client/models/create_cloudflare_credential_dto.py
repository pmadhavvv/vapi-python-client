from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_cloudflare_credential_dto_provider import CreateCloudflareCredentialDTOProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloudflare_r2_bucket_plan import CloudflareR2BucketPlan


T = TypeVar("T", bound="CreateCloudflareCredentialDTO")


@_attrs_define
class CreateCloudflareCredentialDTO:
    """
    Attributes:
        provider (CreateCloudflareCredentialDTOProvider): Credential provider. Only allowed value is cloudflare
        account_id (Union[Unset, str]): Cloudflare Account Id.
        api_key (Union[Unset, str]): Cloudflare API Key / Token.
        account_email (Union[Unset, str]): Cloudflare Account Email.
        bucket_plan (Union[Unset, CloudflareR2BucketPlan]):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateCloudflareCredentialDTOProvider
    account_id: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    account_email: Union[Unset, str] = UNSET
    bucket_plan: Union[Unset, "CloudflareR2BucketPlan"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        account_id = self.account_id

        api_key = self.api_key

        account_email = self.account_email

        bucket_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_plan, Unset):
            bucket_plan = self.bucket_plan.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if account_email is not UNSET:
            field_dict["accountEmail"] = account_email
        if bucket_plan is not UNSET:
            field_dict["bucketPlan"] = bucket_plan
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cloudflare_r2_bucket_plan import CloudflareR2BucketPlan

        d = src_dict.copy()
        provider = CreateCloudflareCredentialDTOProvider(d.pop("provider"))

        account_id = d.pop("accountId", UNSET)

        api_key = d.pop("apiKey", UNSET)

        account_email = d.pop("accountEmail", UNSET)

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, CloudflareR2BucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = CloudflareR2BucketPlan.from_dict(_bucket_plan)

        name = d.pop("name", UNSET)

        create_cloudflare_credential_dto = cls(
            provider=provider,
            account_id=account_id,
            api_key=api_key,
            account_email=account_email,
            bucket_plan=bucket_plan,
            name=name,
        )

        create_cloudflare_credential_dto.additional_properties = d
        return create_cloudflare_credential_dto

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

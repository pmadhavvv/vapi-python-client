from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_supabase_credential_dto_provider import CreateSupabaseCredentialDTOProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supabase_bucket_plan import SupabaseBucketPlan


T = TypeVar("T", bound="CreateSupabaseCredentialDTO")


@_attrs_define
class CreateSupabaseCredentialDTO:
    """
    Attributes:
        provider (CreateSupabaseCredentialDTOProvider): This is for supabase storage.
        bucket_plan (Union[Unset, SupabaseBucketPlan]):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateSupabaseCredentialDTOProvider
    bucket_plan: Union[Unset, "SupabaseBucketPlan"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

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
        if bucket_plan is not UNSET:
            field_dict["bucketPlan"] = bucket_plan
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supabase_bucket_plan import SupabaseBucketPlan

        d = dict(src_dict)
        provider = CreateSupabaseCredentialDTOProvider(d.pop("provider"))

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, SupabaseBucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = SupabaseBucketPlan.from_dict(_bucket_plan)

        name = d.pop("name", UNSET)

        create_supabase_credential_dto = cls(
            provider=provider,
            bucket_plan=bucket_plan,
            name=name,
        )

        create_supabase_credential_dto.additional_properties = d
        return create_supabase_credential_dto

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

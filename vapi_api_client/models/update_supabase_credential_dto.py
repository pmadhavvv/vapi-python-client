from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supabase_bucket_plan import SupabaseBucketPlan


T = TypeVar("T", bound="UpdateSupabaseCredentialDTO")


@_attrs_define
class UpdateSupabaseCredentialDTO:
    """
    Attributes:
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        bucket_plan (Union[Unset, SupabaseBucketPlan]):
    """

    name: Union[Unset, str] = UNSET
    bucket_plan: Union[Unset, "SupabaseBucketPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        bucket_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_plan, Unset):
            bucket_plan = self.bucket_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if bucket_plan is not UNSET:
            field_dict["bucketPlan"] = bucket_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supabase_bucket_plan import SupabaseBucketPlan

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, SupabaseBucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = SupabaseBucketPlan.from_dict(_bucket_plan)

        update_supabase_credential_dto = cls(
            name=name,
            bucket_plan=bucket_plan,
        )

        update_supabase_credential_dto.additional_properties = d
        return update_supabase_credential_dto

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

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.gcp_credential_provider import GcpCredentialProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_plan import BucketPlan
    from ..models.gcp_key import GcpKey


T = TypeVar("T", bound="GcpCredential")


@_attrs_define
class GcpCredential:
    """
    Attributes:
        provider (GcpCredentialProvider):
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        gcp_key (GcpKey):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        bucket_plan (Union[Unset, BucketPlan]):
    """

    provider: GcpCredentialProvider
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    gcp_key: "GcpKey"
    name: Union[Unset, str] = UNSET
    bucket_plan: Union[Unset, "BucketPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        gcp_key = self.gcp_key.to_dict()

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
                "gcpKey": gcp_key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if bucket_plan is not UNSET:
            field_dict["bucketPlan"] = bucket_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_plan import BucketPlan
        from ..models.gcp_key import GcpKey

        d = dict(src_dict)
        provider = GcpCredentialProvider(d.pop("provider"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        gcp_key = GcpKey.from_dict(d.pop("gcpKey"))

        name = d.pop("name", UNSET)

        _bucket_plan = d.pop("bucketPlan", UNSET)
        bucket_plan: Union[Unset, BucketPlan]
        if isinstance(_bucket_plan, Unset):
            bucket_plan = UNSET
        else:
            bucket_plan = BucketPlan.from_dict(_bucket_plan)

        gcp_credential = cls(
            provider=provider,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            gcp_key=gcp_key,
            name=name,
            bucket_plan=bucket_plan,
        )

        gcp_credential.additional_properties = d
        return gcp_credential

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

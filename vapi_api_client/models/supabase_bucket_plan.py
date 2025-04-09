from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supabase_bucket_plan_region import SupabaseBucketPlanRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupabaseBucketPlan")


@_attrs_define
class SupabaseBucketPlan:
    """
    Attributes:
        region (SupabaseBucketPlanRegion): This is the S3 Region. It should look like us-east-1
            It should be one of the supabase regions defined in the SUPABASE_REGION enum
            Check https://supabase.com/docs/guides/platform/regions for up to date regions
        url (str): This is the S3 compatible URL for Supabase S3
            This should look like https://<project-ID>.supabase.co/storage/v1/s3
        access_key_id (str): This is the Supabase S3 Access Key ID.
            The user creates this in the Supabase project Storage settings
        secret_access_key (str): This is the Supabase S3 Secret Access Key.
            The user creates this in the Supabase project Storage settings along with the access key id
        name (str): This is the Supabase S3 Bucket Name.
            The user must create this in Supabase under Storage > Buckets
            A bucket that does not exist will not be checked now, but file uploads will fail
        path (Union[Unset, str]): This is the Supabase S3 Bucket Folder Path.
            The user can create this in Supabase under Storage > Buckets
            A path that does not exist will not be checked now, but file uploads will fail
            A Path is like a folder in the bucket
            Eg. If the bucket is called "my-bucket" and the path is "my-folder", the full path is "my-bucket/my-folder"
    """

    region: SupabaseBucketPlanRegion
    url: str
    access_key_id: str
    secret_access_key: str
    name: str
    path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region.value

        url = self.url

        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        name = self.name

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "url": url,
                "accessKeyId": access_key_id,
                "secretAccessKey": secret_access_key,
                "name": name,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region = SupabaseBucketPlanRegion(d.pop("region"))

        url = d.pop("url")

        access_key_id = d.pop("accessKeyId")

        secret_access_key = d.pop("secretAccessKey")

        name = d.pop("name")

        path = d.pop("path", UNSET)

        supabase_bucket_plan = cls(
            region=region,
            url=url,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            name=name,
            path=path,
        )

        supabase_bucket_plan.additional_properties = d
        return supabase_bucket_plan

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

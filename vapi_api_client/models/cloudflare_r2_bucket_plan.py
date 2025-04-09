from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudflareR2BucketPlan")


@_attrs_define
class CloudflareR2BucketPlan:
    """
    Attributes:
        name (str): This is the name of the bucket.
        access_key_id (Union[Unset, str]): Cloudflare R2 Access key ID.
        secret_access_key (Union[Unset, str]): Cloudflare R2 access key secret. This is not returned in the API.
        url (Union[Unset, str]): Cloudflare R2 base url.
        path (Union[Unset, str]): This is the path where call artifacts will be stored.

            Usage:
            - To store call artifacts in a specific folder, set this to the full path. Eg. "/folder-name1/folder-name2".
            - To store call artifacts in the root of the bucket, leave this blank.

            @default "/"
    """

    name: str
    access_key_id: Union[Unset, str] = UNSET
    secret_access_key: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        url = self.url

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if access_key_id is not UNSET:
            field_dict["accessKeyId"] = access_key_id
        if secret_access_key is not UNSET:
            field_dict["secretAccessKey"] = secret_access_key
        if url is not UNSET:
            field_dict["url"] = url
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        access_key_id = d.pop("accessKeyId", UNSET)

        secret_access_key = d.pop("secretAccessKey", UNSET)

        url = d.pop("url", UNSET)

        path = d.pop("path", UNSET)

        cloudflare_r2_bucket_plan = cls(
            name=name,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            url=url,
            path=path,
        )

        cloudflare_r2_bucket_plan.additional_properties = d
        return cloudflare_r2_bucket_plan

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

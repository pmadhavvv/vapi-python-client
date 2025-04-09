from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BucketPlan")


@_attrs_define
class BucketPlan:
    """
    Attributes:
        name (str): This is the name of the bucket.
        region (Union[Unset, str]): This is the region of the bucket.

            Usage:
            - If `credential.type` is `aws`, then this is required.
            - If `credential.type` is `gcp`, then this is optional since GCP allows buckets to be accessed without a region
            but region is required for data residency requirements. Read here:
            https://cloud.google.com/storage/docs/request-endpoints
        path (Union[Unset, str]): This is the path where call artifacts will be stored.

            Usage:
            - To store call artifacts in a specific folder, set this to the full path. Eg. "/folder-name1/folder-name2".
            - To store call artifacts in the root of the bucket, leave this blank.

            @default "/"
        hmac_access_key (Union[Unset, str]): This is the HMAC access key offered by GCP for interoperability with S3
            clients. Here is the guide on how to create: https://cloud.google.com/storage/docs/authentication/managing-
            hmackeys#console

            Usage:
            - If `credential.type` is `gcp`, then this is required.
            - If `credential.type` is `aws`, then this is not required since credential.awsAccessKeyId is used instead.
        hmac_secret (Union[Unset, str]): This is the secret for the HMAC access key. Here is the guide on how to create:
            https://cloud.google.com/storage/docs/authentication/managing-hmackeys#console

            Usage:
            - If `credential.type` is `gcp`, then this is required.
            - If `credential.type` is `aws`, then this is not required since credential.awsSecretAccessKey is used instead.

            Note: This is not returned in the API.
    """

    name: str
    region: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    hmac_access_key: Union[Unset, str] = UNSET
    hmac_secret: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        region = self.region

        path = self.path

        hmac_access_key = self.hmac_access_key

        hmac_secret = self.hmac_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if path is not UNSET:
            field_dict["path"] = path
        if hmac_access_key is not UNSET:
            field_dict["hmacAccessKey"] = hmac_access_key
        if hmac_secret is not UNSET:
            field_dict["hmacSecret"] = hmac_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        region = d.pop("region", UNSET)

        path = d.pop("path", UNSET)

        hmac_access_key = d.pop("hmacAccessKey", UNSET)

        hmac_secret = d.pop("hmacSecret", UNSET)

        bucket_plan = cls(
            name=name,
            region=region,
            path=path,
            hmac_access_key=hmac_access_key,
            hmac_secret=hmac_secret,
        )

        bucket_plan.additional_properties = d
        return bucket_plan

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

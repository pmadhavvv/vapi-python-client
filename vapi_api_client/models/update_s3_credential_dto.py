from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateS3CredentialDTO")


@_attrs_define
class UpdateS3CredentialDTO:
    """
    Attributes:
        aws_access_key_id (Union[Unset, str]): AWS access key ID.
        aws_secret_access_key (Union[Unset, str]): AWS access key secret. This is not returned in the API.
        region (Union[Unset, str]): AWS region in which the S3 bucket is located.
        s_3_bucket_name (Union[Unset, str]): AWS S3 bucket name.
        s_3_path_prefix (Union[Unset, str]): The path prefix for the uploaded recording. Ex. "recordings/"
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    aws_access_key_id: Union[Unset, str] = UNSET
    aws_secret_access_key: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    s_3_bucket_name: Union[Unset, str] = UNSET
    s_3_path_prefix: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_access_key_id = self.aws_access_key_id

        aws_secret_access_key = self.aws_secret_access_key

        region = self.region

        s_3_bucket_name = self.s_3_bucket_name

        s_3_path_prefix = self.s_3_path_prefix

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_access_key_id is not UNSET:
            field_dict["awsAccessKeyId"] = aws_access_key_id
        if aws_secret_access_key is not UNSET:
            field_dict["awsSecretAccessKey"] = aws_secret_access_key
        if region is not UNSET:
            field_dict["region"] = region
        if s_3_bucket_name is not UNSET:
            field_dict["s3BucketName"] = s_3_bucket_name
        if s_3_path_prefix is not UNSET:
            field_dict["s3PathPrefix"] = s_3_path_prefix
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_access_key_id = d.pop("awsAccessKeyId", UNSET)

        aws_secret_access_key = d.pop("awsSecretAccessKey", UNSET)

        region = d.pop("region", UNSET)

        s_3_bucket_name = d.pop("s3BucketName", UNSET)

        s_3_path_prefix = d.pop("s3PathPrefix", UNSET)

        name = d.pop("name", UNSET)

        update_s3_credential_dto = cls(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region=region,
            s_3_bucket_name=s_3_bucket_name,
            s_3_path_prefix=s_3_path_prefix,
            name=name,
        )

        update_s3_credential_dto.additional_properties = d
        return update_s3_credential_dto

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_s3_credential_dto_provider import CreateS3CredentialDTOProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateS3CredentialDTO")


@_attrs_define
class CreateS3CredentialDTO:
    """
    Attributes:
        provider (CreateS3CredentialDTOProvider): Credential provider. Only allowed value is s3
        aws_access_key_id (str): AWS access key ID.
        aws_secret_access_key (str): AWS access key secret. This is not returned in the API.
        region (str): AWS region in which the S3 bucket is located.
        s_3_bucket_name (str): AWS S3 bucket name.
        s_3_path_prefix (str): The path prefix for the uploaded recording. Ex. "recordings/"
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateS3CredentialDTOProvider
    aws_access_key_id: str
    aws_secret_access_key: str
    region: str
    s_3_bucket_name: str
    s_3_path_prefix: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        aws_access_key_id = self.aws_access_key_id

        aws_secret_access_key = self.aws_secret_access_key

        region = self.region

        s_3_bucket_name = self.s_3_bucket_name

        s_3_path_prefix = self.s_3_path_prefix

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "awsAccessKeyId": aws_access_key_id,
                "awsSecretAccessKey": aws_secret_access_key,
                "region": region,
                "s3BucketName": s_3_bucket_name,
                "s3PathPrefix": s_3_path_prefix,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = CreateS3CredentialDTOProvider(d.pop("provider"))

        aws_access_key_id = d.pop("awsAccessKeyId")

        aws_secret_access_key = d.pop("awsSecretAccessKey")

        region = d.pop("region")

        s_3_bucket_name = d.pop("s3BucketName")

        s_3_path_prefix = d.pop("s3PathPrefix")

        name = d.pop("name", UNSET)

        create_s3_credential_dto = cls(
            provider=provider,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region=region,
            s_3_bucket_name=s_3_bucket_name,
            s_3_path_prefix=s_3_path_prefix,
            name=name,
        )

        create_s3_credential_dto.additional_properties = d
        return create_s3_credential_dto

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

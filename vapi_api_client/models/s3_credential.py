import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.s3_credential_provider import S3CredentialProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3Credential")


@_attrs_define
class S3Credential:
    """
    Attributes:
        provider (S3CredentialProvider): Credential provider. Only allowed value is s3
        aws_access_key_id (str): AWS access key ID.
        aws_secret_access_key (str): AWS access key secret. This is not returned in the API.
        region (str): AWS region in which the S3 bucket is located.
        s_3_bucket_name (str): AWS S3 bucket name.
        s_3_path_prefix (str): The path prefix for the uploaded recording. Ex. "recordings/"
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: S3CredentialProvider
    aws_access_key_id: str
    aws_secret_access_key: str
    region: str
    s_3_bucket_name: str
    s_3_path_prefix: str
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        aws_access_key_id = self.aws_access_key_id

        aws_secret_access_key = self.aws_secret_access_key

        region = self.region

        s_3_bucket_name = self.s_3_bucket_name

        s_3_path_prefix = self.s_3_path_prefix

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = S3CredentialProvider(d.pop("provider"))

        aws_access_key_id = d.pop("awsAccessKeyId")

        aws_secret_access_key = d.pop("awsSecretAccessKey")

        region = d.pop("region")

        s_3_bucket_name = d.pop("s3BucketName")

        s_3_path_prefix = d.pop("s3PathPrefix")

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        name = d.pop("name", UNSET)

        s3_credential = cls(
            provider=provider,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region=region,
            s_3_bucket_name=s_3_bucket_name,
            s_3_path_prefix=s_3_path_prefix,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
        )

        s3_credential.additional_properties = d
        return s3_credential

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

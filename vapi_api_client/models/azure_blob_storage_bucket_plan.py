from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureBlobStorageBucketPlan")


@_attrs_define
class AzureBlobStorageBucketPlan:
    """
    Attributes:
        connection_string (str): This is the blob storage connection string for the Azure resource.
        container_name (str): This is the container name for the Azure blob storage.
        path (Union[Unset, str]): This is the path where call artifacts will be stored.

            Usage:
            - To store call artifacts in a specific folder, set this to the full path. Eg. "/folder-name1/folder-name2".
            - To store call artifacts in the root of the bucket, leave this blank.

            @default "/"
    """

    connection_string: str
    container_name: str
    path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_string = self.connection_string

        container_name = self.container_name

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionString": connection_string,
                "containerName": container_name,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_string = d.pop("connectionString")

        container_name = d.pop("containerName")

        path = d.pop("path", UNSET)

        azure_blob_storage_bucket_plan = cls(
            connection_string=connection_string,
            container_name=container_name,
            path=path,
        )

        azure_blob_storage_bucket_plan.additional_properties = d
        return azure_blob_storage_bucket_plan

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

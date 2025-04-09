import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.file_object import FileObject
from ..models.file_status import FileStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_metadata import FileMetadata


T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """
    Attributes:
        id (str): This is the unique identifier for the file.
        org_id (str): This is the unique identifier for the org that this file belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the file was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the file was last updated.
        object_ (Union[Unset, FileObject]):
        status (Union[Unset, FileStatus]):
        name (Union[Unset, str]): This is the name of the file. This is just for your own reference.
        original_name (Union[Unset, str]):
        bytes_ (Union[Unset, float]):
        purpose (Union[Unset, str]):
        mimetype (Union[Unset, str]):
        key (Union[Unset, str]):
        path (Union[Unset, str]):
        bucket (Union[Unset, str]):
        url (Union[Unset, str]):
        parsed_text_url (Union[Unset, str]):
        parsed_text_bytes (Union[Unset, float]):
        metadata (Union[Unset, FileMetadata]):
    """

    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    object_: Union[Unset, FileObject] = UNSET
    status: Union[Unset, FileStatus] = UNSET
    name: Union[Unset, str] = UNSET
    original_name: Union[Unset, str] = UNSET
    bytes_: Union[Unset, float] = UNSET
    purpose: Union[Unset, str] = UNSET
    mimetype: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    parsed_text_url: Union[Unset, str] = UNSET
    parsed_text_bytes: Union[Unset, float] = UNSET
    metadata: Union[Unset, "FileMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        object_: Union[Unset, str] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name = self.name

        original_name = self.original_name

        bytes_ = self.bytes_

        purpose = self.purpose

        mimetype = self.mimetype

        key = self.key

        path = self.path

        bucket = self.bucket

        url = self.url

        parsed_text_url = self.parsed_text_url

        parsed_text_bytes = self.parsed_text_bytes

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if original_name is not UNSET:
            field_dict["originalName"] = original_name
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if mimetype is not UNSET:
            field_dict["mimetype"] = mimetype
        if key is not UNSET:
            field_dict["key"] = key
        if path is not UNSET:
            field_dict["path"] = path
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if url is not UNSET:
            field_dict["url"] = url
        if parsed_text_url is not UNSET:
            field_dict["parsedTextUrl"] = parsed_text_url
        if parsed_text_bytes is not UNSET:
            field_dict["parsedTextBytes"] = parsed_text_bytes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_metadata import FileMetadata

        d = dict(src_dict)
        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, FileObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = FileObject(_object_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FileStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FileStatus(_status)

        name = d.pop("name", UNSET)

        original_name = d.pop("originalName", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        purpose = d.pop("purpose", UNSET)

        mimetype = d.pop("mimetype", UNSET)

        key = d.pop("key", UNSET)

        path = d.pop("path", UNSET)

        bucket = d.pop("bucket", UNSET)

        url = d.pop("url", UNSET)

        parsed_text_url = d.pop("parsedTextUrl", UNSET)

        parsed_text_bytes = d.pop("parsedTextBytes", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, FileMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = FileMetadata.from_dict(_metadata)

        file = cls(
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            object_=object_,
            status=status,
            name=name,
            original_name=original_name,
            bytes_=bytes_,
            purpose=purpose,
            mimetype=mimetype,
            key=key,
            path=path,
            bucket=bucket,
            url=url,
            parsed_text_url=parsed_text_url,
            parsed_text_bytes=parsed_text_bytes,
            metadata=metadata,
        )

        file.additional_properties = d
        return file

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

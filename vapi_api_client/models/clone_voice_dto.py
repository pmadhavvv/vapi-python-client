from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CloneVoiceDTO")


@_attrs_define
class CloneVoiceDTO:
    """
    Attributes:
        name (str): This is the name of the cloned voice in the provider account.
        files (list[File]): These are the files you want to use to clone your voice. Only Audio files are supported.
        description (Union[Unset, str]): This is the description of your cloned voice.
        labels (Union[Unset, str]): Serialized labels dictionary for the voice.
    """

    name: str
    files: list[File]
    description: Union[Unset, str] = UNSET
    labels: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_tuple()

            files.append(files_item)

        description = self.description

        labels = self.labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "files": files,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = File(payload=BytesIO(files_item_data))

            files.append(files_item)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        clone_voice_dto = cls(
            name=name,
            files=files,
            description=description,
            labels=labels,
        )

        clone_voice_dto.additional_properties = d
        return clone_voice_dto

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

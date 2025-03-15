from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeBaseResponseDocument")


@_attrs_define
class KnowledgeBaseResponseDocument:
    """
    Attributes:
        content (str): This is the content of the document.
        similarity (float): This is the similarity score of the document.
        uuid (Union[Unset, str]): This is the uuid of the document.
    """

    content: str
    similarity: float
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        similarity = self.similarity

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "similarity": similarity,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        similarity = d.pop("similarity")

        uuid = d.pop("uuid", UNSET)

        knowledge_base_response_document = cls(
            content=content,
            similarity=similarity,
            uuid=uuid,
        )

        knowledge_base_response_document.additional_properties = d
        return knowledge_base_response_document

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

from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_base_model import KnowledgeBaseModel
from ..models.knowledge_base_provider import KnowledgeBaseProvider

T = TypeVar("T", bound="KnowledgeBase")


@_attrs_define
class KnowledgeBase:
    """
    Attributes:
        name (str): The name of the knowledge base Example: My Knowledge Base.
        provider (KnowledgeBaseProvider): The provider of the knowledge base Example: google.
        model (KnowledgeBaseModel): The model to use for the knowledge base Example: gemini-1.5-flash.
        description (str): A description of the knowledge base
        file_ids (list[str]): The file IDs associated with this knowledge base
    """

    name: str
    provider: KnowledgeBaseProvider
    model: KnowledgeBaseModel
    description: str
    file_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provider = self.provider.value

        model = self.model.value

        description = self.description

        file_ids = self.file_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "provider": provider,
                "model": model,
                "description": description,
                "fileIds": file_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        provider = KnowledgeBaseProvider(d.pop("provider"))

        model = KnowledgeBaseModel(d.pop("model"))

        description = d.pop("description")

        file_ids = cast(list[str], d.pop("fileIds"))

        knowledge_base = cls(
            name=name,
            provider=provider,
            model=model,
            description=description,
            file_ids=file_ids,
        )

        knowledge_base.additional_properties = d
        return knowledge_base

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

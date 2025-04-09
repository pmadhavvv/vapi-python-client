from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_custom_knowledge_base_dto_provider import CreateCustomKnowledgeBaseDTOProvider

if TYPE_CHECKING:
    from ..models.server import Server


T = TypeVar("T", bound="CreateCustomKnowledgeBaseDTO")


@_attrs_define
class CreateCustomKnowledgeBaseDTO:
    """
    Attributes:
        provider (CreateCustomKnowledgeBaseDTOProvider): This knowledge base is bring your own knowledge base
            implementation.
        server (Server):
    """

    provider: CreateCustomKnowledgeBaseDTOProvider
    server: "Server"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server import Server

        d = dict(src_dict)
        provider = CreateCustomKnowledgeBaseDTOProvider(d.pop("provider"))

        server = Server.from_dict(d.pop("server"))

        create_custom_knowledge_base_dto = cls(
            provider=provider,
            server=server,
        )

        create_custom_knowledge_base_dto.additional_properties = d
        return create_custom_knowledge_base_dto

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_knowledge_base_provider import CustomKnowledgeBaseProvider

if TYPE_CHECKING:
    from ..models.server import Server


T = TypeVar("T", bound="CustomKnowledgeBase")


@_attrs_define
class CustomKnowledgeBase:
    """
    Attributes:
        provider (CustomKnowledgeBaseProvider): This knowledge base is bring your own knowledge base implementation.
        server (Server):
        id (str): This is the id of the knowledge base.
        org_id (str): This is the org id of the knowledge base.
    """

    provider: CustomKnowledgeBaseProvider
    server: "Server"
    id: str
    org_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        server = self.server.to_dict()

        id = self.id

        org_id = self.org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "server": server,
                "id": id,
                "orgId": org_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server import Server

        d = dict(src_dict)
        provider = CustomKnowledgeBaseProvider(d.pop("provider"))

        server = Server.from_dict(d.pop("server"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        custom_knowledge_base = cls(
            provider=provider,
            server=server,
            id=id,
            org_id=org_id,
        )

        custom_knowledge_base.additional_properties = d
        return custom_knowledge_base

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

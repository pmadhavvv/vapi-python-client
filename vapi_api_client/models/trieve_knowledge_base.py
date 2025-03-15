from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trieve_knowledge_base_provider import TrieveKnowledgeBaseProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trieve_knowledge_base_import import TrieveKnowledgeBaseImport
    from ..models.trieve_knowledge_base_search_plan import TrieveKnowledgeBaseSearchPlan


T = TypeVar("T", bound="TrieveKnowledgeBase")


@_attrs_define
class TrieveKnowledgeBase:
    """
    Attributes:
        provider (TrieveKnowledgeBaseProvider): This knowledge base is provided by Trieve.

            To learn more about Trieve, visit https://trieve.ai.
        id (str): This is the id of the knowledge base.
        org_id (str): This is the org id of the knowledge base.
        name (Union[Unset, str]): This is the name of the knowledge base.
        search_plan (Union[Unset, TrieveKnowledgeBaseSearchPlan]):
        create_plan (Union[Unset, TrieveKnowledgeBaseImport]):
    """

    provider: TrieveKnowledgeBaseProvider
    id: str
    org_id: str
    name: Union[Unset, str] = UNSET
    search_plan: Union[Unset, "TrieveKnowledgeBaseSearchPlan"] = UNSET
    create_plan: Union[Unset, "TrieveKnowledgeBaseImport"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        id = self.id

        org_id = self.org_id

        name = self.name

        search_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.search_plan, Unset):
            search_plan = self.search_plan.to_dict()

        create_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.create_plan, Unset):
            create_plan = self.create_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "id": id,
                "orgId": org_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if search_plan is not UNSET:
            field_dict["searchPlan"] = search_plan
        if create_plan is not UNSET:
            field_dict["createPlan"] = create_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.trieve_knowledge_base_import import TrieveKnowledgeBaseImport
        from ..models.trieve_knowledge_base_search_plan import TrieveKnowledgeBaseSearchPlan

        d = src_dict.copy()
        provider = TrieveKnowledgeBaseProvider(d.pop("provider"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        name = d.pop("name", UNSET)

        _search_plan = d.pop("searchPlan", UNSET)
        search_plan: Union[Unset, TrieveKnowledgeBaseSearchPlan]
        if isinstance(_search_plan, Unset):
            search_plan = UNSET
        else:
            search_plan = TrieveKnowledgeBaseSearchPlan.from_dict(_search_plan)

        _create_plan = d.pop("createPlan", UNSET)
        create_plan: Union[Unset, TrieveKnowledgeBaseImport]
        if isinstance(_create_plan, Unset):
            create_plan = UNSET
        else:
            create_plan = TrieveKnowledgeBaseImport.from_dict(_create_plan)

        trieve_knowledge_base = cls(
            provider=provider,
            id=id,
            org_id=org_id,
            name=name,
            search_plan=search_plan,
            create_plan=create_plan,
        )

        trieve_knowledge_base.additional_properties = d
        return trieve_knowledge_base

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

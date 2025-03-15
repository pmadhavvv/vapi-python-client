from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_trieve_knowledge_base_dto_provider import CreateTrieveKnowledgeBaseDTOProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trieve_knowledge_base_import import TrieveKnowledgeBaseImport
    from ..models.trieve_knowledge_base_search_plan import TrieveKnowledgeBaseSearchPlan


T = TypeVar("T", bound="CreateTrieveKnowledgeBaseDTO")


@_attrs_define
class CreateTrieveKnowledgeBaseDTO:
    """
    Attributes:
        provider (CreateTrieveKnowledgeBaseDTOProvider): This knowledge base is provided by Trieve.

            To learn more about Trieve, visit https://trieve.ai.
        name (Union[Unset, str]): This is the name of the knowledge base.
        search_plan (Union[Unset, TrieveKnowledgeBaseSearchPlan]):
        create_plan (Union[Unset, TrieveKnowledgeBaseImport]):
    """

    provider: CreateTrieveKnowledgeBaseDTOProvider
    name: Union[Unset, str] = UNSET
    search_plan: Union[Unset, "TrieveKnowledgeBaseSearchPlan"] = UNSET
    create_plan: Union[Unset, "TrieveKnowledgeBaseImport"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

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
        provider = CreateTrieveKnowledgeBaseDTOProvider(d.pop("provider"))

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

        create_trieve_knowledge_base_dto = cls(
            provider=provider,
            name=name,
            search_plan=search_plan,
            create_plan=create_plan,
        )

        create_trieve_knowledge_base_dto.additional_properties = d
        return create_trieve_knowledge_base_dto

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

from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trieve_knowledge_base_create_type import TrieveKnowledgeBaseCreateType

if TYPE_CHECKING:
    from ..models.trieve_knowledge_base_chunk_plan import TrieveKnowledgeBaseChunkPlan


T = TypeVar("T", bound="TrieveKnowledgeBaseCreate")


@_attrs_define
class TrieveKnowledgeBaseCreate:
    """
    Attributes:
        type_ (TrieveKnowledgeBaseCreateType): This is to create a new dataset on Trieve.
        chunk_plans (list['TrieveKnowledgeBaseChunkPlan']): These are the chunk plans used to create the dataset.
    """

    type_: TrieveKnowledgeBaseCreateType
    chunk_plans: list["TrieveKnowledgeBaseChunkPlan"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        chunk_plans = []
        for chunk_plans_item_data in self.chunk_plans:
            chunk_plans_item = chunk_plans_item_data.to_dict()
            chunk_plans.append(chunk_plans_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "chunkPlans": chunk_plans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.trieve_knowledge_base_chunk_plan import TrieveKnowledgeBaseChunkPlan

        d = src_dict.copy()
        type_ = TrieveKnowledgeBaseCreateType(d.pop("type"))

        chunk_plans = []
        _chunk_plans = d.pop("chunkPlans")
        for chunk_plans_item_data in _chunk_plans:
            chunk_plans_item = TrieveKnowledgeBaseChunkPlan.from_dict(chunk_plans_item_data)

            chunk_plans.append(chunk_plans_item)

        trieve_knowledge_base_create = cls(
            type_=type_,
            chunk_plans=chunk_plans,
        )

        trieve_knowledge_base_create.additional_properties = d
        return trieve_knowledge_base_create

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

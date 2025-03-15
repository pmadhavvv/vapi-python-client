from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trieve_knowledge_base_search_plan_search_type import TrieveKnowledgeBaseSearchPlanSearchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrieveKnowledgeBaseSearchPlan")


@_attrs_define
class TrieveKnowledgeBaseSearchPlan:
    """
    Attributes:
        search_type (TrieveKnowledgeBaseSearchPlanSearchType): This is the search method used when searching for
            relevant chunks from the vector store.
        top_k (Union[Unset, float]): Specifies the number of top chunks to return. This corresponds to the `page_size`
            parameter in Trieve.
        remove_stop_words (Union[Unset, bool]): If true, stop words (specified in server/src/stop-words.txt in the git
            repo) will be removed. This will preserve queries that are entirely stop words.
        score_threshold (Union[Unset, float]): This is the score threshold to filter out chunks with a score below the
            threshold for cosine distance metric. For Manhattan Distance, Euclidean Distance, and Dot Product, it will
            filter out scores above the threshold distance. This threshold applies before weight and bias modifications. If
            not specified, this defaults to no threshold. A threshold of 0 will default to no threshold.
    """

    search_type: TrieveKnowledgeBaseSearchPlanSearchType
    top_k: Union[Unset, float] = UNSET
    remove_stop_words: Union[Unset, bool] = UNSET
    score_threshold: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_type = self.search_type.value

        top_k = self.top_k

        remove_stop_words = self.remove_stop_words

        score_threshold = self.score_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "searchType": search_type,
            }
        )
        if top_k is not UNSET:
            field_dict["topK"] = top_k
        if remove_stop_words is not UNSET:
            field_dict["removeStopWords"] = remove_stop_words
        if score_threshold is not UNSET:
            field_dict["scoreThreshold"] = score_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        search_type = TrieveKnowledgeBaseSearchPlanSearchType(d.pop("searchType"))

        top_k = d.pop("topK", UNSET)

        remove_stop_words = d.pop("removeStopWords", UNSET)

        score_threshold = d.pop("scoreThreshold", UNSET)

        trieve_knowledge_base_search_plan = cls(
            search_type=search_type,
            top_k=top_k,
            remove_stop_words=remove_stop_words,
            score_threshold=score_threshold,
        )

        trieve_knowledge_base_search_plan.additional_properties = d
        return trieve_knowledge_base_search_plan

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

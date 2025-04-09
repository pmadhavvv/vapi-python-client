from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrieveKnowledgeBaseChunkPlan")


@_attrs_define
class TrieveKnowledgeBaseChunkPlan:
    r"""
    Attributes:
        file_ids (Union[Unset, list[str]]): These are the file ids that will be used to create the vector store. To
            upload files, use the `POST /files` endpoint.
        websites (Union[Unset, list[str]]): These are the websites that will be used to create the vector store.
        target_splits_per_chunk (Union[Unset, float]): This is an optional field which allows you to specify the number
            of splits you want per chunk. If not specified, the default 20 is used. However, you may want to use a different
            number.
        split_delimiters (Union[Unset, list[str]]): This is an optional field which allows you to specify the delimiters
            to use when splitting the file before chunking the text. If not specified, the default [.!?\n] are used to split
            into sentences. However, you may want to use spaces or other delimiters.
        rebalance_chunks (Union[Unset, bool]): This is an optional field which allows you to specify whether or not to
            rebalance the chunks created from the file. If not specified, the default true is used. If true, Trieve will
            evenly distribute remainder splits across chunks such that 66 splits with a target_splits_per_chunk of 20 will
            result in 3 chunks with 22 splits each.
    """

    file_ids: Union[Unset, list[str]] = UNSET
    websites: Union[Unset, list[str]] = UNSET
    target_splits_per_chunk: Union[Unset, float] = UNSET
    split_delimiters: Union[Unset, list[str]] = UNSET
    rebalance_chunks: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        websites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.websites, Unset):
            websites = self.websites

        target_splits_per_chunk = self.target_splits_per_chunk

        split_delimiters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.split_delimiters, Unset):
            split_delimiters = self.split_delimiters

        rebalance_chunks = self.rebalance_chunks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_ids is not UNSET:
            field_dict["fileIds"] = file_ids
        if websites is not UNSET:
            field_dict["websites"] = websites
        if target_splits_per_chunk is not UNSET:
            field_dict["targetSplitsPerChunk"] = target_splits_per_chunk
        if split_delimiters is not UNSET:
            field_dict["splitDelimiters"] = split_delimiters
        if rebalance_chunks is not UNSET:
            field_dict["rebalanceChunks"] = rebalance_chunks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_ids = cast(list[str], d.pop("fileIds", UNSET))

        websites = cast(list[str], d.pop("websites", UNSET))

        target_splits_per_chunk = d.pop("targetSplitsPerChunk", UNSET)

        split_delimiters = cast(list[str], d.pop("splitDelimiters", UNSET))

        rebalance_chunks = d.pop("rebalanceChunks", UNSET)

        trieve_knowledge_base_chunk_plan = cls(
            file_ids=file_ids,
            websites=websites,
            target_splits_per_chunk=target_splits_per_chunk,
            split_delimiters=split_delimiters,
            rebalance_chunks=rebalance_chunks,
        )

        trieve_knowledge_base_chunk_plan.additional_properties = d
        return trieve_knowledge_base_chunk_plan

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

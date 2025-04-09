from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TranscriberCostTranscriber")


@_attrs_define
class TranscriberCostTranscriber:
    """This is the transcriber that was used during the call.

    This matches one of the below:
    - `call.assistant.transcriber`,
    - `call.assistantId->transcriber`,
    - `call.squad[n].assistant.transcriber`,
    - `call.squad[n].assistantId->transcriber`,
    - `call.squadId->[n].assistant.transcriber`,
    - `call.squadId->[n].assistantId->transcriber`.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transcriber_cost_transcriber = cls()

        transcriber_cost_transcriber.additional_properties = d
        return transcriber_cost_transcriber

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

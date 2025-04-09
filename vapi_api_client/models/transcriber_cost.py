from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcriber_cost_type import TranscriberCostType

if TYPE_CHECKING:
    from ..models.transcriber_cost_transcriber import TranscriberCostTranscriber


T = TypeVar("T", bound="TranscriberCost")


@_attrs_define
class TranscriberCost:
    """
    Attributes:
        type_ (TranscriberCostType): This is the type of cost, always 'transcriber' for this class.
        transcriber (TranscriberCostTranscriber): This is the transcriber that was used during the call.

            This matches one of the below:
            - `call.assistant.transcriber`,
            - `call.assistantId->transcriber`,
            - `call.squad[n].assistant.transcriber`,
            - `call.squad[n].assistantId->transcriber`,
            - `call.squadId->[n].assistant.transcriber`,
            - `call.squadId->[n].assistantId->transcriber`.
        minutes (float): This is the minutes of `transcriber` usage. This should match `call.endedAt` - `call.startedAt`
            for single assistant calls, while squad calls will have multiple transcriber costs one for each assistant that
            was used.
        cost (float): This is the cost of the component in USD.
    """

    type_: TranscriberCostType
    transcriber: "TranscriberCostTranscriber"
    minutes: float
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        transcriber = self.transcriber.to_dict()

        minutes = self.minutes

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "transcriber": transcriber,
                "minutes": minutes,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcriber_cost_transcriber import TranscriberCostTranscriber

        d = dict(src_dict)
        type_ = TranscriberCostType(d.pop("type"))

        transcriber = TranscriberCostTranscriber.from_dict(d.pop("transcriber"))

        minutes = d.pop("minutes")

        cost = d.pop("cost")

        transcriber_cost = cls(
            type_=type_,
            transcriber=transcriber,
            minutes=minutes,
            cost=cost,
        )

        transcriber_cost.additional_properties = d
        return transcriber_cost

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

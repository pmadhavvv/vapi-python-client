from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscriptionEndpointingPlan")


@_attrs_define
class TranscriptionEndpointingPlan:
    """
    Attributes:
        on_punctuation_seconds (Union[Unset, float]): The minimum number of seconds to wait after transcription ending
            with punctuation before sending a request to the model. Defaults to 0.1.

            This setting exists because the transcriber punctuates the transcription when it's more confident that customer
            has completed a thought.

            @default 0.1 Example: 0.1.
        on_no_punctuation_seconds (Union[Unset, float]): The minimum number of seconds to wait after transcription
            ending without punctuation before sending a request to the model. Defaults to 1.5.

            This setting exists to catch the cases where the transcriber was not confident enough to punctuate the
            transcription, but the customer is done and has been silent for a long time.

            @default 1.5 Example: 1.5.
        on_number_seconds (Union[Unset, float]): The minimum number of seconds to wait after transcription ending with a
            number before sending a request to the model. Defaults to 0.4.

            This setting exists because the transcriber will sometimes punctuate the transcription ending with a number,
            even though the customer hasn't uttered the full number. This happens commonly for long numbers when the
            customer reads the number in chunks.

            @default 0.5 Example: 0.5.
    """

    on_punctuation_seconds: Union[Unset, float] = UNSET
    on_no_punctuation_seconds: Union[Unset, float] = UNSET
    on_number_seconds: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on_punctuation_seconds = self.on_punctuation_seconds

        on_no_punctuation_seconds = self.on_no_punctuation_seconds

        on_number_seconds = self.on_number_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on_punctuation_seconds is not UNSET:
            field_dict["onPunctuationSeconds"] = on_punctuation_seconds
        if on_no_punctuation_seconds is not UNSET:
            field_dict["onNoPunctuationSeconds"] = on_no_punctuation_seconds
        if on_number_seconds is not UNSET:
            field_dict["onNumberSeconds"] = on_number_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        on_punctuation_seconds = d.pop("onPunctuationSeconds", UNSET)

        on_no_punctuation_seconds = d.pop("onNoPunctuationSeconds", UNSET)

        on_number_seconds = d.pop("onNumberSeconds", UNSET)

        transcription_endpointing_plan = cls(
            on_punctuation_seconds=on_punctuation_seconds,
            on_no_punctuation_seconds=on_no_punctuation_seconds,
            on_number_seconds=on_number_seconds,
        )

        transcription_endpointing_plan.additional_properties = d
        return transcription_endpointing_plan

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

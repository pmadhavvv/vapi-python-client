from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopSpeakingPlan")


@_attrs_define
class StopSpeakingPlan:
    """
    Attributes:
        num_words (Union[Unset, float]): This is the number of words that the customer has to say before the assistant
            will stop talking.

            Words like "stop", "actually", "no", etc. will always interrupt immediately regardless of this value.

            Words like "okay", "yeah", "right" will never interrupt.

            When set to 0, `voiceSeconds` is used in addition to the transcriptions to determine the customer has started
            speaking.

            Defaults to 0.

            @default 0
        voice_seconds (Union[Unset, float]): This is the seconds customer has to speak before the assistant stops
            talking. This uses the VAD (Voice Activity Detection) spike to determine if the customer has started speaking.

            Considerations:
            - A lower value might be more responsive but could potentially pick up non-speech sounds.
            - A higher value reduces false positives but might slightly delay the detection of speech onset.

            This is only used if `numWords` is set to 0.

            Defaults to 0.2

            @default 0.2 Example: 0.2.
        backoff_seconds (Union[Unset, float]): This is the seconds to wait before the assistant will start talking again
            after being interrupted.

            Defaults to 1.

            @default 1 Example: 1.
        acknowledgement_phrases (Union[Unset, list[str]]): These are the phrases that will never interrupt the
            assistant, even if numWords threshold is met.
            These are typically acknowledgement or backchanneling phrases. Example: ['i understand', 'i see', 'i got it', 'i
            hear you', 'im listening', 'im with you', 'right', 'okay', 'ok', 'sure', 'alright', 'got it', 'understood',
            'yeah', 'yes', 'uh-huh', 'mm-hmm', 'gotcha', 'mhmm', 'ah', 'yeah okay', 'yeah sure'].
        interruption_phrases (Union[Unset, list[str]]): These are the phrases that will always interrupt the assistant
            immediately, regardless of numWords.
            These are typically phrases indicating disagreement or desire to stop. Example: ['stop', 'shut', 'up', 'enough',
            'quiet', 'silence', 'but', 'dont', 'not', 'no', 'hold', 'wait', 'cut', 'pause', 'nope', 'nah', 'nevermind',
            'never', 'bad', 'actually'].
    """

    num_words: Union[Unset, float] = UNSET
    voice_seconds: Union[Unset, float] = UNSET
    backoff_seconds: Union[Unset, float] = UNSET
    acknowledgement_phrases: Union[Unset, list[str]] = UNSET
    interruption_phrases: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_words = self.num_words

        voice_seconds = self.voice_seconds

        backoff_seconds = self.backoff_seconds

        acknowledgement_phrases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.acknowledgement_phrases, Unset):
            acknowledgement_phrases = self.acknowledgement_phrases

        interruption_phrases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.interruption_phrases, Unset):
            interruption_phrases = self.interruption_phrases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_words is not UNSET:
            field_dict["numWords"] = num_words
        if voice_seconds is not UNSET:
            field_dict["voiceSeconds"] = voice_seconds
        if backoff_seconds is not UNSET:
            field_dict["backoffSeconds"] = backoff_seconds
        if acknowledgement_phrases is not UNSET:
            field_dict["acknowledgementPhrases"] = acknowledgement_phrases
        if interruption_phrases is not UNSET:
            field_dict["interruptionPhrases"] = interruption_phrases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_words = d.pop("numWords", UNSET)

        voice_seconds = d.pop("voiceSeconds", UNSET)

        backoff_seconds = d.pop("backoffSeconds", UNSET)

        acknowledgement_phrases = cast(list[str], d.pop("acknowledgementPhrases", UNSET))

        interruption_phrases = cast(list[str], d.pop("interruptionPhrases", UNSET))

        stop_speaking_plan = cls(
            num_words=num_words,
            voice_seconds=voice_seconds,
            backoff_seconds=backoff_seconds,
            acknowledgement_phrases=acknowledgement_phrases,
            interruption_phrases=interruption_phrases,
        )

        stop_speaking_plan.additional_properties = d
        return stop_speaking_plan

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

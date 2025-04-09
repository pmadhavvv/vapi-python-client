from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gemini_multimodal_live_speech_config import GeminiMultimodalLiveSpeechConfig


T = TypeVar("T", bound="GoogleRealtimeConfig")


@_attrs_define
class GoogleRealtimeConfig:
    """
    Attributes:
        top_p (Union[Unset, float]): This is the nucleus sampling parameter that controls the cumulative probability of
            tokens considered during text generation.
            Only applicable with the Gemini Flash 2.0 Multimodal Live API.
        top_k (Union[Unset, float]): This is the top-k sampling parameter that limits the number of highest probability
            tokens considered during text generation.
            Only applicable with the Gemini Flash 2.0 Multimodal Live API.
        presence_penalty (Union[Unset, float]): This is the presence penalty parameter that influences the model's
            likelihood to repeat information by penalizing tokens based on their presence in the text.
            Only applicable with the Gemini Flash 2.0 Multimodal Live API.
        frequency_penalty (Union[Unset, float]): This is the frequency penalty parameter that influences the model's
            likelihood to repeat tokens by penalizing them based on their frequency in the text.
            Only applicable with the Gemini Flash 2.0 Multimodal Live API.
        speech_config (Union[Unset, GeminiMultimodalLiveSpeechConfig]):
    """

    top_p: Union[Unset, float] = UNSET
    top_k: Union[Unset, float] = UNSET
    presence_penalty: Union[Unset, float] = UNSET
    frequency_penalty: Union[Unset, float] = UNSET
    speech_config: Union[Unset, "GeminiMultimodalLiveSpeechConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_p = self.top_p

        top_k = self.top_k

        presence_penalty = self.presence_penalty

        frequency_penalty = self.frequency_penalty

        speech_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.speech_config, Unset):
            speech_config = self.speech_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_p is not UNSET:
            field_dict["topP"] = top_p
        if top_k is not UNSET:
            field_dict["topK"] = top_k
        if presence_penalty is not UNSET:
            field_dict["presencePenalty"] = presence_penalty
        if frequency_penalty is not UNSET:
            field_dict["frequencyPenalty"] = frequency_penalty
        if speech_config is not UNSET:
            field_dict["speechConfig"] = speech_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gemini_multimodal_live_speech_config import GeminiMultimodalLiveSpeechConfig

        d = dict(src_dict)
        top_p = d.pop("topP", UNSET)

        top_k = d.pop("topK", UNSET)

        presence_penalty = d.pop("presencePenalty", UNSET)

        frequency_penalty = d.pop("frequencyPenalty", UNSET)

        _speech_config = d.pop("speechConfig", UNSET)
        speech_config: Union[Unset, GeminiMultimodalLiveSpeechConfig]
        if isinstance(_speech_config, Unset):
            speech_config = UNSET
        else:
            speech_config = GeminiMultimodalLiveSpeechConfig.from_dict(_speech_config)

        google_realtime_config = cls(
            top_p=top_p,
            top_k=top_k,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            speech_config=speech_config,
        )

        google_realtime_config.additional_properties = d
        return google_realtime_config

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

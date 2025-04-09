from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voicemail_detection_cost_provider import VoicemailDetectionCostProvider
from ..models.voicemail_detection_cost_type import VoicemailDetectionCostType

if TYPE_CHECKING:
    from ..models.voicemail_detection_cost_model import VoicemailDetectionCostModel


T = TypeVar("T", bound="VoicemailDetectionCost")


@_attrs_define
class VoicemailDetectionCost:
    """
    Attributes:
        type_ (VoicemailDetectionCostType): This is the type of cost, always 'voicemail-detection' for this class.
        model (VoicemailDetectionCostModel): This is the model that was used to perform the analysis.
        provider (VoicemailDetectionCostProvider): This is the provider that was used to detect the voicemail.
        prompt_text_tokens (float): This is the number of prompt text tokens used in the voicemail detection.
        prompt_audio_tokens (float): This is the number of prompt audio tokens used in the voicemail detection.
        completion_text_tokens (float): This is the number of completion text tokens used in the voicemail detection.
        completion_audio_tokens (float): This is the number of completion audio tokens used in the voicemail detection.
        cost (float): This is the cost of the component in USD.
    """

    type_: VoicemailDetectionCostType
    model: "VoicemailDetectionCostModel"
    provider: VoicemailDetectionCostProvider
    prompt_text_tokens: float
    prompt_audio_tokens: float
    completion_text_tokens: float
    completion_audio_tokens: float
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        model = self.model.to_dict()

        provider = self.provider.value

        prompt_text_tokens = self.prompt_text_tokens

        prompt_audio_tokens = self.prompt_audio_tokens

        completion_text_tokens = self.completion_text_tokens

        completion_audio_tokens = self.completion_audio_tokens

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "model": model,
                "provider": provider,
                "promptTextTokens": prompt_text_tokens,
                "promptAudioTokens": prompt_audio_tokens,
                "completionTextTokens": completion_text_tokens,
                "completionAudioTokens": completion_audio_tokens,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.voicemail_detection_cost_model import VoicemailDetectionCostModel

        d = dict(src_dict)
        type_ = VoicemailDetectionCostType(d.pop("type"))

        model = VoicemailDetectionCostModel.from_dict(d.pop("model"))

        provider = VoicemailDetectionCostProvider(d.pop("provider"))

        prompt_text_tokens = d.pop("promptTextTokens")

        prompt_audio_tokens = d.pop("promptAudioTokens")

        completion_text_tokens = d.pop("completionTextTokens")

        completion_audio_tokens = d.pop("completionAudioTokens")

        cost = d.pop("cost")

        voicemail_detection_cost = cls(
            type_=type_,
            model=model,
            provider=provider,
            prompt_text_tokens=prompt_text_tokens,
            prompt_audio_tokens=prompt_audio_tokens,
            completion_text_tokens=completion_text_tokens,
            completion_audio_tokens=completion_audio_tokens,
            cost=cost,
        )

        voicemail_detection_cost.additional_properties = d
        return voicemail_detection_cost

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

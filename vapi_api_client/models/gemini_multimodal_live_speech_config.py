from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gemini_multimodal_live_voice_config import GeminiMultimodalLiveVoiceConfig


T = TypeVar("T", bound="GeminiMultimodalLiveSpeechConfig")


@_attrs_define
class GeminiMultimodalLiveSpeechConfig:
    """
    Attributes:
        voice_config (GeminiMultimodalLiveVoiceConfig):
    """

    voice_config: "GeminiMultimodalLiveVoiceConfig"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voice_config = self.voice_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voiceConfig": voice_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gemini_multimodal_live_voice_config import GeminiMultimodalLiveVoiceConfig

        d = dict(src_dict)
        voice_config = GeminiMultimodalLiveVoiceConfig.from_dict(d.pop("voiceConfig"))

        gemini_multimodal_live_speech_config = cls(
            voice_config=voice_config,
        )

        gemini_multimodal_live_speech_config.additional_properties = d
        return gemini_multimodal_live_speech_config

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

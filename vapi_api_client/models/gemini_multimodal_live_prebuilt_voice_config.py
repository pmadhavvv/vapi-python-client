from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gemini_multimodal_live_prebuilt_voice_config_voice_name import (
    GeminiMultimodalLivePrebuiltVoiceConfigVoiceName,
)

T = TypeVar("T", bound="GeminiMultimodalLivePrebuiltVoiceConfig")


@_attrs_define
class GeminiMultimodalLivePrebuiltVoiceConfig:
    """
    Attributes:
        voice_name (GeminiMultimodalLivePrebuiltVoiceConfigVoiceName):
    """

    voice_name: GeminiMultimodalLivePrebuiltVoiceConfigVoiceName
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voice_name = self.voice_name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voiceName": voice_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        voice_name = GeminiMultimodalLivePrebuiltVoiceConfigVoiceName(d.pop("voiceName"))

        gemini_multimodal_live_prebuilt_voice_config = cls(
            voice_name=voice_name,
        )

        gemini_multimodal_live_prebuilt_voice_config.additional_properties = d
        return gemini_multimodal_live_prebuilt_voice_config

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

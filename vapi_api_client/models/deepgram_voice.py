from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deepgram_voice_preset_voice_options import DeepgramVoicePresetVoiceOptions
from ..models.deepgram_voice_provider import DeepgramVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan
    from ..models.fallback_plan import FallbackPlan


T = TypeVar("T", bound="DeepgramVoice")


@_attrs_define
class DeepgramVoice:
    """
    Attributes:
        provider (DeepgramVoiceProvider): This is the voice provider that will be used.
        voice_id (Union[DeepgramVoicePresetVoiceOptions, str]): This is the provider-specific ID that will be used.
        mip_opt_out (Union[Unset, bool]): If set to true, this will add mip_opt_out=true as a query parameter of all API
            requests. See https://developers.deepgram.com/docs/the-deepgram-model-improvement-partnership-program#want-to-
            opt-out

            This will only be used if you are using your own Deepgram API key.

            @default false
        chunk_plan (Union[Unset, ChunkPlan]):
        fallback_plan (Union[Unset, FallbackPlan]):
    """

    provider: DeepgramVoiceProvider
    voice_id: Union[DeepgramVoicePresetVoiceOptions, str]
    mip_opt_out: Union[Unset, bool] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    fallback_plan: Union[Unset, "FallbackPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id: str
        if isinstance(self.voice_id, DeepgramVoicePresetVoiceOptions):
            voice_id = self.voice_id.value
        else:
            voice_id = self.voice_id

        mip_opt_out = self.mip_opt_out

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

        fallback_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fallback_plan, Unset):
            fallback_plan = self.fallback_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "voiceId": voice_id,
            }
        )
        if mip_opt_out is not UNSET:
            field_dict["mipOptOut"] = mip_opt_out
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan
        if fallback_plan is not UNSET:
            field_dict["fallbackPlan"] = fallback_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan
        from ..models.fallback_plan import FallbackPlan

        d = dict(src_dict)
        provider = DeepgramVoiceProvider(d.pop("provider"))

        def _parse_voice_id(data: object) -> Union[DeepgramVoicePresetVoiceOptions, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_id_type_0 = DeepgramVoicePresetVoiceOptions(data)

                return voice_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[DeepgramVoicePresetVoiceOptions, str], data)

        voice_id = _parse_voice_id(d.pop("voiceId"))

        mip_opt_out = d.pop("mipOptOut", UNSET)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        _fallback_plan = d.pop("fallbackPlan", UNSET)
        fallback_plan: Union[Unset, FallbackPlan]
        if isinstance(_fallback_plan, Unset):
            fallback_plan = UNSET
        else:
            fallback_plan = FallbackPlan.from_dict(_fallback_plan)

        deepgram_voice = cls(
            provider=provider,
            voice_id=voice_id,
            mip_opt_out=mip_opt_out,
            chunk_plan=chunk_plan,
            fallback_plan=fallback_plan,
        )

        deepgram_voice.additional_properties = d
        return deepgram_voice

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

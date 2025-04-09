from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hume_voice_model import HumeVoiceModel
from ..models.hume_voice_provider import HumeVoiceProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_plan import ChunkPlan
    from ..models.fallback_plan import FallbackPlan


T = TypeVar("T", bound="HumeVoice")


@_attrs_define
class HumeVoice:
    """
    Attributes:
        provider (HumeVoiceProvider): This is the voice provider that will be used.
        voice_id (str): The ID of the particular voice you want to use.
        model (Union[Unset, HumeVoiceModel]): This is the model that will be used. Example: octave.
        is_custom_hume_voice (Union[Unset, bool]): Indicates whether the chosen voice is a preset Hume AI voice or a
            custom voice.
        chunk_plan (Union[Unset, ChunkPlan]):
        description (Union[Unset, str]): Natural language instructions describing how the synthesized speech should
            sound, including but not limited to tone, intonation, pacing, and accent (e.g., 'a soft, gentle voice with a
            strong British accent').

            If a Voice is specified in the request, this description serves as acting instructions.
            If no Voice is specified, a new voice is generated based on this description.
        fallback_plan (Union[Unset, FallbackPlan]):
    """

    provider: HumeVoiceProvider
    voice_id: str
    model: Union[Unset, HumeVoiceModel] = UNSET
    is_custom_hume_voice: Union[Unset, bool] = UNSET
    chunk_plan: Union[Unset, "ChunkPlan"] = UNSET
    description: Union[Unset, str] = UNSET
    fallback_plan: Union[Unset, "FallbackPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        voice_id = self.voice_id

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        is_custom_hume_voice = self.is_custom_hume_voice

        chunk_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chunk_plan, Unset):
            chunk_plan = self.chunk_plan.to_dict()

        description = self.description

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
        if model is not UNSET:
            field_dict["model"] = model
        if is_custom_hume_voice is not UNSET:
            field_dict["isCustomHumeVoice"] = is_custom_hume_voice
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan
        if description is not UNSET:
            field_dict["description"] = description
        if fallback_plan is not UNSET:
            field_dict["fallbackPlan"] = fallback_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_plan import ChunkPlan
        from ..models.fallback_plan import FallbackPlan

        d = dict(src_dict)
        provider = HumeVoiceProvider(d.pop("provider"))

        voice_id = d.pop("voiceId")

        _model = d.pop("model", UNSET)
        model: Union[Unset, HumeVoiceModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = HumeVoiceModel(_model)

        is_custom_hume_voice = d.pop("isCustomHumeVoice", UNSET)

        _chunk_plan = d.pop("chunkPlan", UNSET)
        chunk_plan: Union[Unset, ChunkPlan]
        if isinstance(_chunk_plan, Unset):
            chunk_plan = UNSET
        else:
            chunk_plan = ChunkPlan.from_dict(_chunk_plan)

        description = d.pop("description", UNSET)

        _fallback_plan = d.pop("fallbackPlan", UNSET)
        fallback_plan: Union[Unset, FallbackPlan]
        if isinstance(_fallback_plan, Unset):
            fallback_plan = UNSET
        else:
            fallback_plan = FallbackPlan.from_dict(_fallback_plan)

        hume_voice = cls(
            provider=provider,
            voice_id=voice_id,
            model=model,
            is_custom_hume_voice=is_custom_hume_voice,
            chunk_plan=chunk_plan,
            description=description,
            fallback_plan=fallback_plan,
        )

        hume_voice.additional_properties = d
        return hume_voice

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

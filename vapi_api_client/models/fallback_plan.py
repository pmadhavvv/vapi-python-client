from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fallback_azure_voice import FallbackAzureVoice
    from ..models.fallback_cartesia_voice import FallbackCartesiaVoice
    from ..models.fallback_custom_voice import FallbackCustomVoice
    from ..models.fallback_deepgram_voice import FallbackDeepgramVoice
    from ..models.fallback_eleven_labs_voice import FallbackElevenLabsVoice
    from ..models.fallback_hume_voice import FallbackHumeVoice
    from ..models.fallback_lmnt_voice import FallbackLMNTVoice
    from ..models.fallback_neets_voice import FallbackNeetsVoice
    from ..models.fallback_open_ai_voice import FallbackOpenAIVoice
    from ..models.fallback_play_ht_voice import FallbackPlayHTVoice
    from ..models.fallback_rime_ai_voice import FallbackRimeAIVoice
    from ..models.fallback_smallest_ai_voice import FallbackSmallestAIVoice
    from ..models.fallback_tavus_voice import FallbackTavusVoice
    from ..models.fallback_vapi_voice import FallbackVapiVoice


T = TypeVar("T", bound="FallbackPlan")


@_attrs_define
class FallbackPlan:
    """
    Attributes:
        voices (list[Union['FallbackAzureVoice', 'FallbackCartesiaVoice', 'FallbackCustomVoice',
            'FallbackDeepgramVoice', 'FallbackElevenLabsVoice', 'FallbackHumeVoice', 'FallbackLMNTVoice',
            'FallbackNeetsVoice', 'FallbackOpenAIVoice', 'FallbackPlayHTVoice', 'FallbackRimeAIVoice',
            'FallbackSmallestAIVoice', 'FallbackTavusVoice', 'FallbackVapiVoice']]): This is the list of voices to fallback
            to in the event that the primary voice provider fails.
    """

    voices: list[
        Union[
            "FallbackAzureVoice",
            "FallbackCartesiaVoice",
            "FallbackCustomVoice",
            "FallbackDeepgramVoice",
            "FallbackElevenLabsVoice",
            "FallbackHumeVoice",
            "FallbackLMNTVoice",
            "FallbackNeetsVoice",
            "FallbackOpenAIVoice",
            "FallbackPlayHTVoice",
            "FallbackRimeAIVoice",
            "FallbackSmallestAIVoice",
            "FallbackTavusVoice",
            "FallbackVapiVoice",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fallback_azure_voice import FallbackAzureVoice
        from ..models.fallback_cartesia_voice import FallbackCartesiaVoice
        from ..models.fallback_custom_voice import FallbackCustomVoice
        from ..models.fallback_deepgram_voice import FallbackDeepgramVoice
        from ..models.fallback_eleven_labs_voice import FallbackElevenLabsVoice
        from ..models.fallback_hume_voice import FallbackHumeVoice
        from ..models.fallback_lmnt_voice import FallbackLMNTVoice
        from ..models.fallback_neets_voice import FallbackNeetsVoice
        from ..models.fallback_open_ai_voice import FallbackOpenAIVoice
        from ..models.fallback_play_ht_voice import FallbackPlayHTVoice
        from ..models.fallback_rime_ai_voice import FallbackRimeAIVoice
        from ..models.fallback_smallest_ai_voice import FallbackSmallestAIVoice
        from ..models.fallback_vapi_voice import FallbackVapiVoice

        voices = []
        for voices_item_data in self.voices:
            voices_item: dict[str, Any]
            if isinstance(voices_item_data, FallbackAzureVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackCartesiaVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackHumeVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackCustomVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackDeepgramVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackElevenLabsVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackVapiVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackLMNTVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackNeetsVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackOpenAIVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackPlayHTVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackRimeAIVoice):
                voices_item = voices_item_data.to_dict()
            elif isinstance(voices_item_data, FallbackSmallestAIVoice):
                voices_item = voices_item_data.to_dict()
            else:
                voices_item = voices_item_data.to_dict()

            voices.append(voices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voices": voices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.fallback_azure_voice import FallbackAzureVoice
        from ..models.fallback_cartesia_voice import FallbackCartesiaVoice
        from ..models.fallback_custom_voice import FallbackCustomVoice
        from ..models.fallback_deepgram_voice import FallbackDeepgramVoice
        from ..models.fallback_eleven_labs_voice import FallbackElevenLabsVoice
        from ..models.fallback_hume_voice import FallbackHumeVoice
        from ..models.fallback_lmnt_voice import FallbackLMNTVoice
        from ..models.fallback_neets_voice import FallbackNeetsVoice
        from ..models.fallback_open_ai_voice import FallbackOpenAIVoice
        from ..models.fallback_play_ht_voice import FallbackPlayHTVoice
        from ..models.fallback_rime_ai_voice import FallbackRimeAIVoice
        from ..models.fallback_smallest_ai_voice import FallbackSmallestAIVoice
        from ..models.fallback_tavus_voice import FallbackTavusVoice
        from ..models.fallback_vapi_voice import FallbackVapiVoice

        d = src_dict.copy()
        voices = []
        _voices = d.pop("voices")
        for voices_item_data in _voices:

            def _parse_voices_item(
                data: object,
            ) -> Union[
                "FallbackAzureVoice",
                "FallbackCartesiaVoice",
                "FallbackCustomVoice",
                "FallbackDeepgramVoice",
                "FallbackElevenLabsVoice",
                "FallbackHumeVoice",
                "FallbackLMNTVoice",
                "FallbackNeetsVoice",
                "FallbackOpenAIVoice",
                "FallbackPlayHTVoice",
                "FallbackRimeAIVoice",
                "FallbackSmallestAIVoice",
                "FallbackTavusVoice",
                "FallbackVapiVoice",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_0 = FallbackAzureVoice.from_dict(data)

                    return voices_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_1 = FallbackCartesiaVoice.from_dict(data)

                    return voices_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_2 = FallbackHumeVoice.from_dict(data)

                    return voices_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_3 = FallbackCustomVoice.from_dict(data)

                    return voices_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_4 = FallbackDeepgramVoice.from_dict(data)

                    return voices_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_5 = FallbackElevenLabsVoice.from_dict(data)

                    return voices_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_6 = FallbackVapiVoice.from_dict(data)

                    return voices_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_7 = FallbackLMNTVoice.from_dict(data)

                    return voices_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_8 = FallbackNeetsVoice.from_dict(data)

                    return voices_item_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_9 = FallbackOpenAIVoice.from_dict(data)

                    return voices_item_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_10 = FallbackPlayHTVoice.from_dict(data)

                    return voices_item_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_11 = FallbackRimeAIVoice.from_dict(data)

                    return voices_item_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    voices_item_type_12 = FallbackSmallestAIVoice.from_dict(data)

                    return voices_item_type_12
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                voices_item_type_13 = FallbackTavusVoice.from_dict(data)

                return voices_item_type_13

            voices_item = _parse_voices_item(voices_item_data)

            voices.append(voices_item)

        fallback_plan = cls(
            voices=voices,
        )

        fallback_plan.additional_properties = d
        return fallback_plan

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

from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_cost_breakdown import AnalysisCostBreakdown


T = TypeVar("T", bound="CostBreakdown")


@_attrs_define
class CostBreakdown:
    """
    Attributes:
        transport (Union[Unset, float]): This is the cost of the transport provider, like Twilio or Vonage.
        stt (Union[Unset, float]): This is the cost of the speech-to-text service.
        llm (Union[Unset, float]): This is the cost of the language model.
        tts (Union[Unset, float]): This is the cost of the text-to-speech service.
        vapi (Union[Unset, float]): This is the cost of Vapi.
        total (Union[Unset, float]): This is the total cost of the call.
        llm_prompt_tokens (Union[Unset, float]): This is the LLM prompt tokens used for the call.
        llm_completion_tokens (Union[Unset, float]): This is the LLM completion tokens used for the call.
        tts_characters (Union[Unset, float]): This is the TTS characters used for the call.
        analysis_cost_breakdown (Union[Unset, AnalysisCostBreakdown]):
    """

    transport: Union[Unset, float] = UNSET
    stt: Union[Unset, float] = UNSET
    llm: Union[Unset, float] = UNSET
    tts: Union[Unset, float] = UNSET
    vapi: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    llm_prompt_tokens: Union[Unset, float] = UNSET
    llm_completion_tokens: Union[Unset, float] = UNSET
    tts_characters: Union[Unset, float] = UNSET
    analysis_cost_breakdown: Union[Unset, "AnalysisCostBreakdown"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transport = self.transport

        stt = self.stt

        llm = self.llm

        tts = self.tts

        vapi = self.vapi

        total = self.total

        llm_prompt_tokens = self.llm_prompt_tokens

        llm_completion_tokens = self.llm_completion_tokens

        tts_characters = self.tts_characters

        analysis_cost_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.analysis_cost_breakdown, Unset):
            analysis_cost_breakdown = self.analysis_cost_breakdown.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transport is not UNSET:
            field_dict["transport"] = transport
        if stt is not UNSET:
            field_dict["stt"] = stt
        if llm is not UNSET:
            field_dict["llm"] = llm
        if tts is not UNSET:
            field_dict["tts"] = tts
        if vapi is not UNSET:
            field_dict["vapi"] = vapi
        if total is not UNSET:
            field_dict["total"] = total
        if llm_prompt_tokens is not UNSET:
            field_dict["llmPromptTokens"] = llm_prompt_tokens
        if llm_completion_tokens is not UNSET:
            field_dict["llmCompletionTokens"] = llm_completion_tokens
        if tts_characters is not UNSET:
            field_dict["ttsCharacters"] = tts_characters
        if analysis_cost_breakdown is not UNSET:
            field_dict["analysisCostBreakdown"] = analysis_cost_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.analysis_cost_breakdown import AnalysisCostBreakdown

        d = src_dict.copy()
        transport = d.pop("transport", UNSET)

        stt = d.pop("stt", UNSET)

        llm = d.pop("llm", UNSET)

        tts = d.pop("tts", UNSET)

        vapi = d.pop("vapi", UNSET)

        total = d.pop("total", UNSET)

        llm_prompt_tokens = d.pop("llmPromptTokens", UNSET)

        llm_completion_tokens = d.pop("llmCompletionTokens", UNSET)

        tts_characters = d.pop("ttsCharacters", UNSET)

        _analysis_cost_breakdown = d.pop("analysisCostBreakdown", UNSET)
        analysis_cost_breakdown: Union[Unset, AnalysisCostBreakdown]
        if isinstance(_analysis_cost_breakdown, Unset):
            analysis_cost_breakdown = UNSET
        else:
            analysis_cost_breakdown = AnalysisCostBreakdown.from_dict(_analysis_cost_breakdown)

        cost_breakdown = cls(
            transport=transport,
            stt=stt,
            llm=llm,
            tts=tts,
            vapi=vapi,
            total=total,
            llm_prompt_tokens=llm_prompt_tokens,
            llm_completion_tokens=llm_completion_tokens,
            tts_characters=tts_characters,
            analysis_cost_breakdown=analysis_cost_breakdown,
        )

        cost_breakdown.additional_properties = d
        return cost_breakdown

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

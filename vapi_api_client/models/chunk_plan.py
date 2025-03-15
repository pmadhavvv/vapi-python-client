from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chunk_plan_punctuation_boundaries import ChunkPlanPunctuationBoundaries
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.format_plan import FormatPlan


T = TypeVar("T", bound="ChunkPlan")


@_attrs_define
class ChunkPlan:
    """
    Attributes:
        enabled (Union[Unset, bool]): This determines whether the model output is chunked before being sent to the voice
            provider. Default `true`.

            Usage:
            - To rely on the voice provider's audio generation logic, set this to `false`.
            - If seeing issues with quality, set this to `true`.

            If disabled, Vapi-provided audio control tokens like <flush /> will not work.

            @default true Example: True.
        min_characters (Union[Unset, float]): This is the minimum number of characters in a chunk.

            Usage:
            - To increase quality, set this to a higher value.
            - To decrease latency, set this to a lower value.

            @default 30 Example: 30.
        punctuation_boundaries (Union[Unset, ChunkPlanPunctuationBoundaries]): These are the punctuations that are
            considered valid boundaries for a chunk to be created.

            Usage:
            - To increase quality, constrain to fewer boundaries.
            - To decrease latency, enable all.

            Default is automatically set to balance the trade-off between quality and latency based on the provider.
            Example: ['。', '，', '.', '!', '?', ';', '،', '۔', '।', '॥', '|', '||', ',', ':'].
        format_plan (Union[Unset, FormatPlan]):
    """

    enabled: Union[Unset, bool] = UNSET
    min_characters: Union[Unset, float] = UNSET
    punctuation_boundaries: Union[Unset, ChunkPlanPunctuationBoundaries] = UNSET
    format_plan: Union[Unset, "FormatPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        min_characters = self.min_characters

        punctuation_boundaries: Union[Unset, str] = UNSET
        if not isinstance(self.punctuation_boundaries, Unset):
            punctuation_boundaries = self.punctuation_boundaries.value

        format_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.format_plan, Unset):
            format_plan = self.format_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if min_characters is not UNSET:
            field_dict["minCharacters"] = min_characters
        if punctuation_boundaries is not UNSET:
            field_dict["punctuationBoundaries"] = punctuation_boundaries
        if format_plan is not UNSET:
            field_dict["formatPlan"] = format_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.format_plan import FormatPlan

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        min_characters = d.pop("minCharacters", UNSET)

        _punctuation_boundaries = d.pop("punctuationBoundaries", UNSET)
        punctuation_boundaries: Union[Unset, ChunkPlanPunctuationBoundaries]
        if isinstance(_punctuation_boundaries, Unset):
            punctuation_boundaries = UNSET
        else:
            punctuation_boundaries = ChunkPlanPunctuationBoundaries(_punctuation_boundaries)

        _format_plan = d.pop("formatPlan", UNSET)
        format_plan: Union[Unset, FormatPlan]
        if isinstance(_format_plan, Unset):
            format_plan = UNSET
        else:
            format_plan = FormatPlan.from_dict(_format_plan)

        chunk_plan = cls(
            enabled=enabled,
            min_characters=min_characters,
            punctuation_boundaries=punctuation_boundaries,
            format_plan=format_plan,
        )

        chunk_plan.additional_properties = d
        return chunk_plan

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

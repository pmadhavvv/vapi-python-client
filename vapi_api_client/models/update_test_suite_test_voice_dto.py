from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_suite_test_scorer_ai import TestSuiteTestScorerAI


T = TypeVar("T", bound="UpdateTestSuiteTestVoiceDto")


@_attrs_define
class UpdateTestSuiteTestVoiceDto:
    """
    Attributes:
        scorers (Union[Unset, list['TestSuiteTestScorerAI']]): These are the scorers used to evaluate the test.
        name (Union[Unset, str]): This is the name of the test.
        script (Union[Unset, str]): This is the script to be used for the voice test.
        num_attempts (Union[Unset, float]): This is the number of attempts allowed for the test.
    """

    scorers: Union[Unset, list["TestSuiteTestScorerAI"]] = UNSET
    name: Union[Unset, str] = UNSET
    script: Union[Unset, str] = UNSET
    num_attempts: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scorers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scorers, Unset):
            scorers = []
            for scorers_item_data in self.scorers:
                scorers_item = scorers_item_data.to_dict()
                scorers.append(scorers_item)

        name = self.name

        script = self.script

        num_attempts = self.num_attempts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scorers is not UNSET:
            field_dict["scorers"] = scorers
        if name is not UNSET:
            field_dict["name"] = name
        if script is not UNSET:
            field_dict["script"] = script
        if num_attempts is not UNSET:
            field_dict["numAttempts"] = num_attempts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_suite_test_scorer_ai import TestSuiteTestScorerAI

        d = dict(src_dict)
        scorers = []
        _scorers = d.pop("scorers", UNSET)
        for scorers_item_data in _scorers or []:
            scorers_item = TestSuiteTestScorerAI.from_dict(scorers_item_data)

            scorers.append(scorers_item)

        name = d.pop("name", UNSET)

        script = d.pop("script", UNSET)

        num_attempts = d.pop("numAttempts", UNSET)

        update_test_suite_test_voice_dto = cls(
            scorers=scorers,
            name=name,
            script=script,
            num_attempts=num_attempts,
        )

        update_test_suite_test_voice_dto.additional_properties = d
        return update_test_suite_test_voice_dto

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

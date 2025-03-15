from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_test_suite_test_voice_dto_type import CreateTestSuiteTestVoiceDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_suite_test_scorer_ai import TestSuiteTestScorerAI


T = TypeVar("T", bound="CreateTestSuiteTestVoiceDto")


@_attrs_define
class CreateTestSuiteTestVoiceDto:
    """
    Attributes:
        scorers (list['TestSuiteTestScorerAI']): These are the scorers used to evaluate the test.
        type_ (CreateTestSuiteTestVoiceDtoType): This is the type of the test, which must be voice.
        script (str): This is the script to be used for the voice test.
        num_attempts (Union[Unset, float]): This is the number of attempts allowed for the test.
        name (Union[Unset, str]): This is the name of the test.
    """

    scorers: list["TestSuiteTestScorerAI"]
    type_: CreateTestSuiteTestVoiceDtoType
    script: str
    num_attempts: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scorers = []
        for scorers_item_data in self.scorers:
            scorers_item = scorers_item_data.to_dict()
            scorers.append(scorers_item)

        type_ = self.type_.value

        script = self.script

        num_attempts = self.num_attempts

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scorers": scorers,
                "type": type_,
                "script": script,
            }
        )
        if num_attempts is not UNSET:
            field_dict["numAttempts"] = num_attempts
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.test_suite_test_scorer_ai import TestSuiteTestScorerAI

        d = src_dict.copy()
        scorers = []
        _scorers = d.pop("scorers")
        for scorers_item_data in _scorers:
            scorers_item = TestSuiteTestScorerAI.from_dict(scorers_item_data)

            scorers.append(scorers_item)

        type_ = CreateTestSuiteTestVoiceDtoType(d.pop("type"))

        script = d.pop("script")

        num_attempts = d.pop("numAttempts", UNSET)

        name = d.pop("name", UNSET)

        create_test_suite_test_voice_dto = cls(
            scorers=scorers,
            type_=type_,
            script=script,
            num_attempts=num_attempts,
            name=name,
        )

        create_test_suite_test_voice_dto.additional_properties = d
        return create_test_suite_test_voice_dto

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

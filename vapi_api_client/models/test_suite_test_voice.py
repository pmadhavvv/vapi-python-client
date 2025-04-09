import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.test_suite_test_voice_type import TestSuiteTestVoiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_suite_test_scorer_ai import TestSuiteTestScorerAI


T = TypeVar("T", bound="TestSuiteTestVoice")


@_attrs_define
class TestSuiteTestVoice:
    """
    Attributes:
        scorers (list['TestSuiteTestScorerAI']): These are the scorers used to evaluate the test.
        type_ (TestSuiteTestVoiceType): This is the type of the test, which must be voice.
        id (str): This is the unique identifier for the test.
        test_suite_id (str): This is the unique identifier for the test suite this test belongs to.
        org_id (str): This is the unique identifier for the organization this test belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the test was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the test was last updated.
        script (str): This is the script to be used for the voice test.
        name (Union[Unset, str]): This is the name of the test.
        num_attempts (Union[Unset, float]): This is the number of attempts allowed for the test.
    """

    scorers: list["TestSuiteTestScorerAI"]
    type_: TestSuiteTestVoiceType
    id: str
    test_suite_id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    script: str
    name: Union[Unset, str] = UNSET
    num_attempts: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scorers = []
        for scorers_item_data in self.scorers:
            scorers_item = scorers_item_data.to_dict()
            scorers.append(scorers_item)

        type_ = self.type_.value

        id = self.id

        test_suite_id = self.test_suite_id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        script = self.script

        name = self.name

        num_attempts = self.num_attempts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scorers": scorers,
                "type": type_,
                "id": id,
                "testSuiteId": test_suite_id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "script": script,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if num_attempts is not UNSET:
            field_dict["numAttempts"] = num_attempts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_suite_test_scorer_ai import TestSuiteTestScorerAI

        d = dict(src_dict)
        scorers = []
        _scorers = d.pop("scorers")
        for scorers_item_data in _scorers:
            scorers_item = TestSuiteTestScorerAI.from_dict(scorers_item_data)

            scorers.append(scorers_item)

        type_ = TestSuiteTestVoiceType(d.pop("type"))

        id = d.pop("id")

        test_suite_id = d.pop("testSuiteId")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        script = d.pop("script")

        name = d.pop("name", UNSET)

        num_attempts = d.pop("numAttempts", UNSET)

        test_suite_test_voice = cls(
            scorers=scorers,
            type_=type_,
            id=id,
            test_suite_id=test_suite_id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            script=script,
            name=name,
            num_attempts=num_attempts,
        )

        test_suite_test_voice.additional_properties = d
        return test_suite_test_voice

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

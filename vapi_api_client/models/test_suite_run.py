import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.test_suite_run_status import TestSuiteRunStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_suite_run_test_result import TestSuiteRunTestResult


T = TypeVar("T", bound="TestSuiteRun")


@_attrs_define
class TestSuiteRun:
    """
    Attributes:
        status (TestSuiteRunStatus): This is the current status of the test suite run.
        id (str): This is the unique identifier for the test suite run.
        org_id (str): This is the unique identifier for the organization this run belongs to.
        test_suite_id (str): This is the unique identifier for the test suite this run belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the test suite run was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the test suite run was last
            updated.
        test_results (list['TestSuiteRunTestResult']): These are the results of the tests in this test suite run.
        name (Union[Unset, str]): This is the name of the test suite run.
    """

    status: TestSuiteRunStatus
    id: str
    org_id: str
    test_suite_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    test_results: list["TestSuiteRunTestResult"]
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        id = self.id

        org_id = self.org_id

        test_suite_id = self.test_suite_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        test_results = []
        for test_results_item_data in self.test_results:
            test_results_item = test_results_item_data.to_dict()
            test_results.append(test_results_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "id": id,
                "orgId": org_id,
                "testSuiteId": test_suite_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "testResults": test_results,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_suite_run_test_result import TestSuiteRunTestResult

        d = dict(src_dict)
        status = TestSuiteRunStatus(d.pop("status"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        test_suite_id = d.pop("testSuiteId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        test_results = []
        _test_results = d.pop("testResults")
        for test_results_item_data in _test_results:
            test_results_item = TestSuiteRunTestResult.from_dict(test_results_item_data)

            test_results.append(test_results_item)

        name = d.pop("name", UNSET)

        test_suite_run = cls(
            status=status,
            id=id,
            org_id=org_id,
            test_suite_id=test_suite_id,
            created_at=created_at,
            updated_at=updated_at,
            test_results=test_results,
            name=name,
        )

        test_suite_run.additional_properties = d
        return test_suite_run

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

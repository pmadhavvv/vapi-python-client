from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscriptPlan")


@_attrs_define
class TranscriptPlan:
    """
    Attributes:
        enabled (Union[Unset, bool]): This determines whether the transcript is stored in `call.artifact.transcript`.
            Defaults to true.

            @default true Example: True.
        assistant_name (Union[Unset, str]): This is the name of the assistant in the transcript. Defaults to 'AI'.

            Usage:
            - If you want to change the name of the assistant in the transcript, set this. Example, here is what the
            transcript would look like with `assistantName` set to 'Buyer':
            ```
            User: Hello, how are you?
            Buyer: I'm fine.
            User: Do you want to buy a car?
            Buyer: No.
            ```

            @default 'AI'
        user_name (Union[Unset, str]): This is the name of the user in the transcript. Defaults to 'User'.

            Usage:
            - If you want to change the name of the user in the transcript, set this. Example, here is what the transcript
            would look like with `userName` set to 'Seller':
            ```
            Seller: Hello, how are you?
            AI: I'm fine.
            Seller: Do you want to buy a car?
            AI: No.
            ```

            @default 'User'
    """

    enabled: Union[Unset, bool] = UNSET
    assistant_name: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        assistant_name = self.assistant_name

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if assistant_name is not UNSET:
            field_dict["assistantName"] = assistant_name
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        assistant_name = d.pop("assistantName", UNSET)

        user_name = d.pop("userName", UNSET)

        transcript_plan = cls(
            enabled=enabled,
            assistant_name=assistant_name,
            user_name=user_name,
        )

        transcript_plan.additional_properties = d
        return transcript_plan

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

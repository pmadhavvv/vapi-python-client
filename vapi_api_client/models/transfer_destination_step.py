from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_destination_step_type import TransferDestinationStepType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_message import CustomMessage


T = TypeVar("T", bound="TransferDestinationStep")


@_attrs_define
class TransferDestinationStep:
    """
    Attributes:
        type_ (TransferDestinationStepType):
        step_name (str): This is the step to transfer to.
        message (Union['CustomMessage', Unset, str]): This is spoken to the customer before connecting them to the
            destination.

            Usage:
            - If this is not provided and transfer tool messages is not provided, default is "Transferring the call now".
            - If set to "", nothing is spoken. This is useful when you want to silently transfer. This is especially useful
            when transferring between assistants in a squad. In this scenario, you likely also want to set
            `assistant.firstMessageMode=assistant-speaks-first-with-model-generated-message` for the destination assistant.

            This accepts a string or a ToolMessageStart class. Latter is useful if you want to specify multiple messages for
            different languages through the `contents` field.
        description (Union[Unset, str]): This is the description of the destination, used by the AI to choose when and
            how to transfer the call.
    """

    type_: TransferDestinationStepType
    step_name: str
    message: Union["CustomMessage", Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_message import CustomMessage

        type_ = self.type_.value

        step_name = self.step_name

        message: Union[Unset, dict[str, Any], str]
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, CustomMessage):
            message = self.message.to_dict()
        else:
            message = self.message

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "stepName": step_name,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.custom_message import CustomMessage

        d = src_dict.copy()
        type_ = TransferDestinationStepType(d.pop("type"))

        step_name = d.pop("stepName")

        def _parse_message(data: object) -> Union["CustomMessage", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_1 = CustomMessage.from_dict(data)

                return message_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CustomMessage", Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        description = d.pop("description", UNSET)

        transfer_destination_step = cls(
            type_=type_,
            step_name=step_name,
            message=message,
            description=description,
        )

        transfer_destination_step.additional_properties = d
        return transfer_destination_step

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

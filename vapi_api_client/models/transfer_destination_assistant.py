from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_destination_assistant_transfer_mode import TransferDestinationAssistantTransferMode
from ..models.transfer_destination_assistant_type import TransferDestinationAssistantType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_message import CustomMessage


T = TypeVar("T", bound="TransferDestinationAssistant")


@_attrs_define
class TransferDestinationAssistant:
    """
    Attributes:
        type_ (TransferDestinationAssistantType):
        assistant_name (str): This is the assistant to transfer the call to.
        message (Union['CustomMessage', Unset, str]): This is spoken to the customer before connecting them to the
            destination.

            Usage:
            - If this is not provided and transfer tool messages is not provided, default is "Transferring the call now".
            - If set to "", nothing is spoken. This is useful when you want to silently transfer. This is especially useful
            when transferring between assistants in a squad. In this scenario, you likely also want to set
            `assistant.firstMessageMode=assistant-speaks-first-with-model-generated-message` for the destination assistant.

            This accepts a string or a ToolMessageStart class. Latter is useful if you want to specify multiple messages for
            different languages through the `contents` field.
        transfer_mode (Union[Unset, TransferDestinationAssistantTransferMode]): This is the mode to use for the
            transfer. Defaults to `rolling-history`.

            - `rolling-history`: This is the default mode. It keeps the entire conversation history and appends the new
            assistant's system message on transfer.

              Example:

              Pre-transfer:
                system: assistant1 system message
                assistant: assistant1 first message
                user: hey, good morning
                assistant: how can i help?
                user: i need help with my account
                assistant: (destination.message)

              Post-transfer:
                system: assistant1 system message
                assistant: assistant1 first message
                user: hey, good morning
                assistant: how can i help?
                user: i need help with my account
                assistant: (destination.message)
                system: assistant2 system message
                assistant: assistant2 first message (or model generated if firstMessageMode is set to `assistant-speaks-
            first-with-model-generated-message`)

            - `swap-system-message-in-history`: This replaces the original system message with the new assistant's system
            message on transfer.

              Example:

              Pre-transfer:
                system: assistant1 system message
                assistant: assistant1 first message
                user: hey, good morning
                assistant: how can i help?
                user: i need help with my account
                assistant: (destination.message)

              Post-transfer:
                system: assistant2 system message
                assistant: assistant1 first message
                user: hey, good morning
                assistant: how can i help?
                user: i need help with my account
                assistant: (destination.message)
                assistant: assistant2 first message (or model generated if firstMessageMode is set to `assistant-speaks-
            first-with-model-generated-message`)

            - `delete-history`: This deletes the entire conversation history on transfer.

              Example:

              Pre-transfer:
                system: assistant1 system message
                assistant: assistant1 first message
                user: hey, good morning
                assistant: how can i help?
                user: i need help with my account
                assistant: (destination.message)

              Post-transfer:
                system: assistant2 system message
                assistant: assistant2 first message
                user: Yes, please
                assistant: how can i help?
                user: i need help with my account

            - `swap-system-message-in-history-and-remove-transfer-tool-messages`: This replaces the original system message
            with the new assistant's system message on transfer and removes transfer tool messages from conversation history
            sent to the LLM.

              Example:

              Pre-transfer:
                system: assistant1 system message
                assistant: assistant1 first message
                user: hey, good morning
                assistant: how can i help?
                user: i need help with my account
                transfer-tool
                transfer-tool-result
                assistant: (destination.message)

              Post-transfer:
                system: assistant2 system message
                assistant: assistant1 first message
                user: hey, good morning
                assistant: how can i help?
                user: i need help with my account
                assistant: (destination.message)
                assistant: assistant2 first message (or model generated if firstMessageMode is set to `assistant-speaks-
            first-with-model-generated-message`)

            @default 'rolling-history'
        description (Union[Unset, str]): This is the description of the destination, used by the AI to choose when and
            how to transfer the call.
    """

    type_: TransferDestinationAssistantType
    assistant_name: str
    message: Union["CustomMessage", Unset, str] = UNSET
    transfer_mode: Union[Unset, TransferDestinationAssistantTransferMode] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_message import CustomMessage

        type_ = self.type_.value

        assistant_name = self.assistant_name

        message: Union[Unset, dict[str, Any], str]
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, CustomMessage):
            message = self.message.to_dict()
        else:
            message = self.message

        transfer_mode: Union[Unset, str] = UNSET
        if not isinstance(self.transfer_mode, Unset):
            transfer_mode = self.transfer_mode.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "assistantName": assistant_name,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if transfer_mode is not UNSET:
            field_dict["transferMode"] = transfer_mode
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.custom_message import CustomMessage

        d = src_dict.copy()
        type_ = TransferDestinationAssistantType(d.pop("type"))

        assistant_name = d.pop("assistantName")

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

        _transfer_mode = d.pop("transferMode", UNSET)
        transfer_mode: Union[Unset, TransferDestinationAssistantTransferMode]
        if isinstance(_transfer_mode, Unset):
            transfer_mode = UNSET
        else:
            transfer_mode = TransferDestinationAssistantTransferMode(_transfer_mode)

        description = d.pop("description", UNSET)

        transfer_destination_assistant = cls(
            type_=type_,
            assistant_name=assistant_name,
            message=message,
            transfer_mode=transfer_mode,
            description=description,
        )

        transfer_destination_assistant.additional_properties = d
        return transfer_destination_assistant

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

from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_message_tool_calls_type import ServerMessageToolCallsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact import Artifact
    from ..models.bash_tool_with_tool_call import BashToolWithToolCall
    from ..models.call import Call
    from ..models.computer_tool_with_tool_call import ComputerToolWithToolCall
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
    from ..models.create_customer_dto import CreateCustomerDTO
    from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
    from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
    from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
    from ..models.function_tool_with_tool_call import FunctionToolWithToolCall
    from ..models.ghl_tool_with_tool_call import GhlToolWithToolCall
    from ..models.make_tool_with_tool_call import MakeToolWithToolCall
    from ..models.text_editor_tool_with_tool_call import TextEditorToolWithToolCall
    from ..models.tool_call import ToolCall


T = TypeVar("T", bound="ServerMessageToolCalls")


@_attrs_define
class ServerMessageToolCalls:
    """
    Attributes:
        tool_with_tool_call_list (list[Union['BashToolWithToolCall', 'ComputerToolWithToolCall',
            'FunctionToolWithToolCall', 'GhlToolWithToolCall', 'MakeToolWithToolCall', 'TextEditorToolWithToolCall']]): This
            is the list of tools calls that the model is requesting along with the original tool configuration.
        tool_call_list (list['ToolCall']): This is the list of tool calls that the model is requesting.
        phone_number (Union['CreateByoPhoneNumberDTO', 'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO',
            'CreateVonagePhoneNumberDTO', Unset]): This is the phone number associated with the call.

            This matches one of the following:
            - `call.phoneNumber`,
            - `call.phoneNumberId`.
        type_ (Union[Unset, ServerMessageToolCallsType]): This is the type of the message. "tool-calls" is sent to call
            a tool.
        timestamp (Union[Unset, str]): This is the ISO-8601 formatted timestamp of when the message was sent.
        artifact (Union[Unset, Artifact]):
        assistant (Union[Unset, CreateAssistantDTO]):
        customer (Union[Unset, CreateCustomerDTO]):
        call (Union[Unset, Call]):
    """

    tool_with_tool_call_list: list[
        Union[
            "BashToolWithToolCall",
            "ComputerToolWithToolCall",
            "FunctionToolWithToolCall",
            "GhlToolWithToolCall",
            "MakeToolWithToolCall",
            "TextEditorToolWithToolCall",
        ]
    ]
    tool_call_list: list["ToolCall"]
    phone_number: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
        Unset,
    ] = UNSET
    type_: Union[Unset, ServerMessageToolCallsType] = UNSET
    timestamp: Union[Unset, str] = UNSET
    artifact: Union[Unset, "Artifact"] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    call: Union[Unset, "Call"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bash_tool_with_tool_call import BashToolWithToolCall
        from ..models.computer_tool_with_tool_call import ComputerToolWithToolCall
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.function_tool_with_tool_call import FunctionToolWithToolCall
        from ..models.ghl_tool_with_tool_call import GhlToolWithToolCall
        from ..models.make_tool_with_tool_call import MakeToolWithToolCall

        tool_with_tool_call_list = []
        for tool_with_tool_call_list_item_data in self.tool_with_tool_call_list:
            tool_with_tool_call_list_item: dict[str, Any]
            if isinstance(tool_with_tool_call_list_item_data, FunctionToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, GhlToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, MakeToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, BashToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, ComputerToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            else:
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()

            tool_with_tool_call_list.append(tool_with_tool_call_list_item)

        tool_call_list = []
        for tool_call_list_item_data in self.tool_call_list:
            tool_call_list_item = tool_call_list_item_data.to_dict()
            tool_call_list.append(tool_call_list_item)

        phone_number: Union[Unset, dict[str, Any]]
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        elif isinstance(self.phone_number, CreateByoPhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        elif isinstance(self.phone_number, CreateTwilioPhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        elif isinstance(self.phone_number, CreateVonagePhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        else:
            phone_number = self.phone_number.to_dict()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        timestamp = self.timestamp

        artifact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artifact, Unset):
            artifact = self.artifact.to_dict()

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        customer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        call: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.call, Unset):
            call = self.call.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toolWithToolCallList": tool_with_tool_call_list,
                "toolCallList": tool_call_list,
            }
        )
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if customer is not UNSET:
            field_dict["customer"] = customer
        if call is not UNSET:
            field_dict["call"] = call

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.artifact import Artifact
        from ..models.bash_tool_with_tool_call import BashToolWithToolCall
        from ..models.call import Call
        from ..models.computer_tool_with_tool_call import ComputerToolWithToolCall
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_customer_dto import CreateCustomerDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.function_tool_with_tool_call import FunctionToolWithToolCall
        from ..models.ghl_tool_with_tool_call import GhlToolWithToolCall
        from ..models.make_tool_with_tool_call import MakeToolWithToolCall
        from ..models.text_editor_tool_with_tool_call import TextEditorToolWithToolCall
        from ..models.tool_call import ToolCall

        d = src_dict.copy()
        tool_with_tool_call_list = []
        _tool_with_tool_call_list = d.pop("toolWithToolCallList")
        for tool_with_tool_call_list_item_data in _tool_with_tool_call_list:

            def _parse_tool_with_tool_call_list_item(
                data: object,
            ) -> Union[
                "BashToolWithToolCall",
                "ComputerToolWithToolCall",
                "FunctionToolWithToolCall",
                "GhlToolWithToolCall",
                "MakeToolWithToolCall",
                "TextEditorToolWithToolCall",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_0 = FunctionToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_1 = GhlToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_2 = MakeToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_3 = BashToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_4 = ComputerToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                tool_with_tool_call_list_item_type_5 = TextEditorToolWithToolCall.from_dict(data)

                return tool_with_tool_call_list_item_type_5

            tool_with_tool_call_list_item = _parse_tool_with_tool_call_list_item(tool_with_tool_call_list_item_data)

            tool_with_tool_call_list.append(tool_with_tool_call_list_item)

        tool_call_list = []
        _tool_call_list = d.pop("toolCallList")
        for tool_call_list_item_data in _tool_call_list:
            tool_call_list_item = ToolCall.from_dict(tool_call_list_item_data)

            tool_call_list.append(tool_call_list_item)

        def _parse_phone_number(
            data: object,
        ) -> Union[
            "CreateByoPhoneNumberDTO",
            "CreateTwilioPhoneNumberDTO",
            "CreateVapiPhoneNumberDTO",
            "CreateVonagePhoneNumberDTO",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_0 = CreateByoPhoneNumberDTO.from_dict(data)

                return phone_number_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_1 = CreateTwilioPhoneNumberDTO.from_dict(data)

                return phone_number_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_2 = CreateVonagePhoneNumberDTO.from_dict(data)

                return phone_number_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            phone_number_type_3 = CreateVapiPhoneNumberDTO.from_dict(data)

            return phone_number_type_3

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ServerMessageToolCallsType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServerMessageToolCallsType(_type_)

        timestamp = d.pop("timestamp", UNSET)

        _artifact = d.pop("artifact", UNSET)
        artifact: Union[Unset, Artifact]
        if isinstance(_artifact, Unset):
            artifact = UNSET
        else:
            artifact = Artifact.from_dict(_artifact)

        _assistant = d.pop("assistant", UNSET)
        assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_assistant, Unset):
            assistant = UNSET
        else:
            assistant = CreateAssistantDTO.from_dict(_assistant)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CreateCustomerDTO]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CreateCustomerDTO.from_dict(_customer)

        _call = d.pop("call", UNSET)
        call: Union[Unset, Call]
        if isinstance(_call, Unset):
            call = UNSET
        else:
            call = Call.from_dict(_call)

        server_message_tool_calls = cls(
            tool_with_tool_call_list=tool_with_tool_call_list,
            tool_call_list=tool_call_list,
            phone_number=phone_number,
            type_=type_,
            timestamp=timestamp,
            artifact=artifact,
            assistant=assistant,
            customer=customer,
            call=call,
        )

        server_message_tool_calls.additional_properties = d
        return server_message_tool_calls

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

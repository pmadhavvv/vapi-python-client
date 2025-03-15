from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_transfer_call_tool_dto_type import CreateTransferCallToolDTOType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_function import OpenAIFunction
    from ..models.server import Server
    from ..models.tool_message_complete import ToolMessageComplete
    from ..models.tool_message_delayed import ToolMessageDelayed
    from ..models.tool_message_failed import ToolMessageFailed
    from ..models.tool_message_start import ToolMessageStart
    from ..models.transfer_destination_assistant import TransferDestinationAssistant
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip
    from ..models.transfer_destination_step import TransferDestinationStep


T = TypeVar("T", bound="CreateTransferCallToolDTO")


@_attrs_define
class CreateTransferCallToolDTO:
    """
    Attributes:
        type_ (CreateTransferCallToolDTOType):
        async_ (Union[Unset, bool]): This determines if the tool is async.

            If async, the assistant will move forward without waiting for your server to respond. This is useful if you just
            want to trigger something on your server.

            If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with
            the result from your server.

            Defaults to synchronous (`false`).
        messages (Union[Unset, list[Union['ToolMessageComplete', 'ToolMessageDelayed', 'ToolMessageFailed',
            'ToolMessageStart']]]): These are the messages that will be spoken to the user as the tool is running.

            For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the
            function tool, these can be custom configured.
        destinations (Union[Unset, list[Union['TransferDestinationAssistant', 'TransferDestinationNumber',
            'TransferDestinationSip', 'TransferDestinationStep']]]): These are the destinations that the call can be
            transferred to. If no destinations are provided, server.url will be used to get the transfer destination once
            the tool is called.
        function (Union[Unset, OpenAIFunction]):
        server (Union[Unset, Server]):
    """

    type_: CreateTransferCallToolDTOType
    async_: Union[Unset, bool] = UNSET
    messages: Union[
        Unset, list[Union["ToolMessageComplete", "ToolMessageDelayed", "ToolMessageFailed", "ToolMessageStart"]]
    ] = UNSET
    destinations: Union[
        Unset,
        list[
            Union[
                "TransferDestinationAssistant",
                "TransferDestinationNumber",
                "TransferDestinationSip",
                "TransferDestinationStep",
            ]
        ],
    ] = UNSET
    function: Union[Unset, "OpenAIFunction"] = UNSET
    server: Union[Unset, "Server"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_message_complete import ToolMessageComplete
        from ..models.tool_message_failed import ToolMessageFailed
        from ..models.tool_message_start import ToolMessageStart
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_step import TransferDestinationStep

        type_ = self.type_.value

        async_ = self.async_

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item: dict[str, Any]
                if isinstance(messages_item_data, ToolMessageStart):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, ToolMessageComplete):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, ToolMessageFailed):
                    messages_item = messages_item_data.to_dict()
                else:
                    messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        destinations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = []
            for destinations_item_data in self.destinations:
                destinations_item: dict[str, Any]
                if isinstance(destinations_item_data, TransferDestinationAssistant):
                    destinations_item = destinations_item_data.to_dict()
                elif isinstance(destinations_item_data, TransferDestinationStep):
                    destinations_item = destinations_item_data.to_dict()
                elif isinstance(destinations_item_data, TransferDestinationNumber):
                    destinations_item = destinations_item_data.to_dict()
                else:
                    destinations_item = destinations_item_data.to_dict()

                destinations.append(destinations_item)

        function: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.function, Unset):
            function = self.function.to_dict()

        server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if async_ is not UNSET:
            field_dict["async"] = async_
        if messages is not UNSET:
            field_dict["messages"] = messages
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if function is not UNSET:
            field_dict["function"] = function
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_ai_function import OpenAIFunction
        from ..models.server import Server
        from ..models.tool_message_complete import ToolMessageComplete
        from ..models.tool_message_delayed import ToolMessageDelayed
        from ..models.tool_message_failed import ToolMessageFailed
        from ..models.tool_message_start import ToolMessageStart
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip
        from ..models.transfer_destination_step import TransferDestinationStep

        d = src_dict.copy()
        type_ = CreateTransferCallToolDTOType(d.pop("type"))

        async_ = d.pop("async", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:

            def _parse_messages_item(
                data: object,
            ) -> Union["ToolMessageComplete", "ToolMessageDelayed", "ToolMessageFailed", "ToolMessageStart"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_0 = ToolMessageStart.from_dict(data)

                    return messages_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_1 = ToolMessageComplete.from_dict(data)

                    return messages_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_2 = ToolMessageFailed.from_dict(data)

                    return messages_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                messages_item_type_3 = ToolMessageDelayed.from_dict(data)

                return messages_item_type_3

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)

        destinations = []
        _destinations = d.pop("destinations", UNSET)
        for destinations_item_data in _destinations or []:

            def _parse_destinations_item(
                data: object,
            ) -> Union[
                "TransferDestinationAssistant",
                "TransferDestinationNumber",
                "TransferDestinationSip",
                "TransferDestinationStep",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    destinations_item_type_0 = TransferDestinationAssistant.from_dict(data)

                    return destinations_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    destinations_item_type_1 = TransferDestinationStep.from_dict(data)

                    return destinations_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    destinations_item_type_2 = TransferDestinationNumber.from_dict(data)

                    return destinations_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                destinations_item_type_3 = TransferDestinationSip.from_dict(data)

                return destinations_item_type_3

            destinations_item = _parse_destinations_item(destinations_item_data)

            destinations.append(destinations_item)

        _function = d.pop("function", UNSET)
        function: Union[Unset, OpenAIFunction]
        if isinstance(_function, Unset):
            function = UNSET
        else:
            function = OpenAIFunction.from_dict(_function)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        create_transfer_call_tool_dto = cls(
            type_=type_,
            async_=async_,
            messages=messages,
            destinations=destinations,
            function=function,
            server=server,
        )

        create_transfer_call_tool_dto.additional_properties = d
        return create_transfer_call_tool_dto

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

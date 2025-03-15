from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deep_infra_model_provider import DeepInfraModelProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_custom_knowledge_base_dto import CreateCustomKnowledgeBaseDTO
    from ..models.create_dtmf_tool_dto import CreateDtmfToolDTO
    from ..models.create_end_call_tool_dto import CreateEndCallToolDTO
    from ..models.create_function_tool_dto import CreateFunctionToolDTO
    from ..models.create_ghl_tool_dto import CreateGhlToolDTO
    from ..models.create_make_tool_dto import CreateMakeToolDTO
    from ..models.create_query_tool_dto import CreateQueryToolDTO
    from ..models.create_transfer_call_tool_dto import CreateTransferCallToolDTO
    from ..models.create_voicemail_tool_dto import CreateVoicemailToolDTO
    from ..models.open_ai_message import OpenAIMessage


T = TypeVar("T", bound="DeepInfraModel")


@_attrs_define
class DeepInfraModel:
    """
    Attributes:
        provider (DeepInfraModelProvider):
        model (str): This is the name of the model. Ex. cognitivecomputations/dolphin-mixtral-8x7b
        messages (Union[Unset, list['OpenAIMessage']]): This is the starting state for the conversation.
        tools (Union[Unset, list[Union['CreateDtmfToolDTO', 'CreateEndCallToolDTO', 'CreateFunctionToolDTO',
            'CreateGhlToolDTO', 'CreateMakeToolDTO', 'CreateQueryToolDTO', 'CreateTransferCallToolDTO',
            'CreateVoicemailToolDTO']]]): These are the tools that the assistant can use during the call. To use existing
            tools, use `toolIds`.

            Both `tools` and `toolIds` can be used together.
        tool_ids (Union[Unset, list[str]]): These are the tools that the assistant can use during the call. To use
            transient tools, use `tools`.

            Both `tools` and `toolIds` can be used together.
        knowledge_base (Union[Unset, CreateCustomKnowledgeBaseDTO]):
        knowledge_base_id (Union[Unset, str]): This is the ID of the knowledge base the model will use.
        temperature (Union[Unset, float]): This is the temperature that will be used for calls. Default is 0 to leverage
            caching for lower latency.
        max_tokens (Union[Unset, float]): This is the max number of tokens that the assistant will be allowed to
            generate in each turn of the conversation. Default is 250.
        emotion_recognition_enabled (Union[Unset, bool]): This determines whether we detect user's emotion while they
            speak and send it as an additional info to model.

            Default `false` because the model is usually are good at understanding the user's emotion from text.

            @default false
        num_fast_turns (Union[Unset, float]): This sets how many turns at the start of the conversation to use a
            smaller, faster model from the same provider before switching to the primary model. Example, gpt-3.5-turbo if
            provider is openai.

            Default is 0.

            @default 0
    """

    provider: DeepInfraModelProvider
    model: str
    messages: Union[Unset, list["OpenAIMessage"]] = UNSET
    tools: Union[
        Unset,
        list[
            Union[
                "CreateDtmfToolDTO",
                "CreateEndCallToolDTO",
                "CreateFunctionToolDTO",
                "CreateGhlToolDTO",
                "CreateMakeToolDTO",
                "CreateQueryToolDTO",
                "CreateTransferCallToolDTO",
                "CreateVoicemailToolDTO",
            ]
        ],
    ] = UNSET
    tool_ids: Union[Unset, list[str]] = UNSET
    knowledge_base: Union[Unset, "CreateCustomKnowledgeBaseDTO"] = UNSET
    knowledge_base_id: Union[Unset, str] = UNSET
    temperature: Union[Unset, float] = UNSET
    max_tokens: Union[Unset, float] = UNSET
    emotion_recognition_enabled: Union[Unset, bool] = UNSET
    num_fast_turns: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_dtmf_tool_dto import CreateDtmfToolDTO
        from ..models.create_end_call_tool_dto import CreateEndCallToolDTO
        from ..models.create_function_tool_dto import CreateFunctionToolDTO
        from ..models.create_ghl_tool_dto import CreateGhlToolDTO
        from ..models.create_make_tool_dto import CreateMakeToolDTO
        from ..models.create_transfer_call_tool_dto import CreateTransferCallToolDTO
        from ..models.create_voicemail_tool_dto import CreateVoicemailToolDTO

        provider = self.provider.value

        model = self.model

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        tools: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item: dict[str, Any]
                if isinstance(tools_item_data, CreateDtmfToolDTO):
                    tools_item = tools_item_data.to_dict()
                elif isinstance(tools_item_data, CreateEndCallToolDTO):
                    tools_item = tools_item_data.to_dict()
                elif isinstance(tools_item_data, CreateVoicemailToolDTO):
                    tools_item = tools_item_data.to_dict()
                elif isinstance(tools_item_data, CreateFunctionToolDTO):
                    tools_item = tools_item_data.to_dict()
                elif isinstance(tools_item_data, CreateGhlToolDTO):
                    tools_item = tools_item_data.to_dict()
                elif isinstance(tools_item_data, CreateMakeToolDTO):
                    tools_item = tools_item_data.to_dict()
                elif isinstance(tools_item_data, CreateTransferCallToolDTO):
                    tools_item = tools_item_data.to_dict()
                else:
                    tools_item = tools_item_data.to_dict()

                tools.append(tools_item)

        tool_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tool_ids, Unset):
            tool_ids = self.tool_ids

        knowledge_base: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.knowledge_base, Unset):
            knowledge_base = self.knowledge_base.to_dict()

        knowledge_base_id = self.knowledge_base_id

        temperature = self.temperature

        max_tokens = self.max_tokens

        emotion_recognition_enabled = self.emotion_recognition_enabled

        num_fast_turns = self.num_fast_turns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "model": model,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages
        if tools is not UNSET:
            field_dict["tools"] = tools
        if tool_ids is not UNSET:
            field_dict["toolIds"] = tool_ids
        if knowledge_base is not UNSET:
            field_dict["knowledgeBase"] = knowledge_base
        if knowledge_base_id is not UNSET:
            field_dict["knowledgeBaseId"] = knowledge_base_id
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if max_tokens is not UNSET:
            field_dict["maxTokens"] = max_tokens
        if emotion_recognition_enabled is not UNSET:
            field_dict["emotionRecognitionEnabled"] = emotion_recognition_enabled
        if num_fast_turns is not UNSET:
            field_dict["numFastTurns"] = num_fast_turns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_custom_knowledge_base_dto import CreateCustomKnowledgeBaseDTO
        from ..models.create_dtmf_tool_dto import CreateDtmfToolDTO
        from ..models.create_end_call_tool_dto import CreateEndCallToolDTO
        from ..models.create_function_tool_dto import CreateFunctionToolDTO
        from ..models.create_ghl_tool_dto import CreateGhlToolDTO
        from ..models.create_make_tool_dto import CreateMakeToolDTO
        from ..models.create_query_tool_dto import CreateQueryToolDTO
        from ..models.create_transfer_call_tool_dto import CreateTransferCallToolDTO
        from ..models.create_voicemail_tool_dto import CreateVoicemailToolDTO
        from ..models.open_ai_message import OpenAIMessage

        d = src_dict.copy()
        provider = DeepInfraModelProvider(d.pop("provider"))

        model = d.pop("model")

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = OpenAIMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        tools = []
        _tools = d.pop("tools", UNSET)
        for tools_item_data in _tools or []:

            def _parse_tools_item(
                data: object,
            ) -> Union[
                "CreateDtmfToolDTO",
                "CreateEndCallToolDTO",
                "CreateFunctionToolDTO",
                "CreateGhlToolDTO",
                "CreateMakeToolDTO",
                "CreateQueryToolDTO",
                "CreateTransferCallToolDTO",
                "CreateVoicemailToolDTO",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_0 = CreateDtmfToolDTO.from_dict(data)

                    return tools_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_1 = CreateEndCallToolDTO.from_dict(data)

                    return tools_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_2 = CreateVoicemailToolDTO.from_dict(data)

                    return tools_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_3 = CreateFunctionToolDTO.from_dict(data)

                    return tools_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_4 = CreateGhlToolDTO.from_dict(data)

                    return tools_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_5 = CreateMakeToolDTO.from_dict(data)

                    return tools_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_6 = CreateTransferCallToolDTO.from_dict(data)

                    return tools_item_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                tools_item_type_7 = CreateQueryToolDTO.from_dict(data)

                return tools_item_type_7

            tools_item = _parse_tools_item(tools_item_data)

            tools.append(tools_item)

        tool_ids = cast(list[str], d.pop("toolIds", UNSET))

        _knowledge_base = d.pop("knowledgeBase", UNSET)
        knowledge_base: Union[Unset, CreateCustomKnowledgeBaseDTO]
        if isinstance(_knowledge_base, Unset):
            knowledge_base = UNSET
        else:
            knowledge_base = CreateCustomKnowledgeBaseDTO.from_dict(_knowledge_base)

        knowledge_base_id = d.pop("knowledgeBaseId", UNSET)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("maxTokens", UNSET)

        emotion_recognition_enabled = d.pop("emotionRecognitionEnabled", UNSET)

        num_fast_turns = d.pop("numFastTurns", UNSET)

        deep_infra_model = cls(
            provider=provider,
            model=model,
            messages=messages,
            tools=tools,
            tool_ids=tool_ids,
            knowledge_base=knowledge_base,
            knowledge_base_id=knowledge_base_id,
            temperature=temperature,
            max_tokens=max_tokens,
            emotion_recognition_enabled=emotion_recognition_enabled,
            num_fast_turns=num_fast_turns,
        )

        deep_infra_model.additional_properties = d
        return deep_infra_model

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

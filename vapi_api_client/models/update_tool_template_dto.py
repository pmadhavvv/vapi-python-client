from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_tool_template_dto_provider import UpdateToolTemplateDTOProvider
from ..models.update_tool_template_dto_type import UpdateToolTemplateDTOType
from ..models.update_tool_template_dto_visibility import UpdateToolTemplateDTOVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_dtmf_tool_dto import CreateDtmfToolDTO
    from ..models.create_end_call_tool_dto import CreateEndCallToolDTO
    from ..models.create_function_tool_dto import CreateFunctionToolDTO
    from ..models.create_ghl_tool_dto import CreateGhlToolDTO
    from ..models.create_make_tool_dto import CreateMakeToolDTO
    from ..models.create_transfer_call_tool_dto import CreateTransferCallToolDTO
    from ..models.create_voicemail_tool_dto import CreateVoicemailToolDTO
    from ..models.function_tool_provider_details import FunctionToolProviderDetails
    from ..models.ghl_tool_provider_details import GhlToolProviderDetails
    from ..models.make_tool_provider_details import MakeToolProviderDetails
    from ..models.tool_template_metadata import ToolTemplateMetadata


T = TypeVar("T", bound="UpdateToolTemplateDTO")


@_attrs_define
class UpdateToolTemplateDTO:
    """
    Attributes:
        type_ (UpdateToolTemplateDTOType):
        details (Union['CreateDtmfToolDTO', 'CreateEndCallToolDTO', 'CreateFunctionToolDTO', 'CreateGhlToolDTO',
            'CreateMakeToolDTO', 'CreateTransferCallToolDTO', 'CreateVoicemailToolDTO', Unset]):
        provider_details (Union['FunctionToolProviderDetails', 'GhlToolProviderDetails', 'MakeToolProviderDetails',
            Unset]):
        metadata (Union[Unset, ToolTemplateMetadata]):
        visibility (Union[Unset, UpdateToolTemplateDTOVisibility]):
        name (Union[Unset, str]): The name of the template. This is just for your own reference.
        provider (Union[Unset, UpdateToolTemplateDTOProvider]):
    """

    type_: UpdateToolTemplateDTOType
    details: Union[
        "CreateDtmfToolDTO",
        "CreateEndCallToolDTO",
        "CreateFunctionToolDTO",
        "CreateGhlToolDTO",
        "CreateMakeToolDTO",
        "CreateTransferCallToolDTO",
        "CreateVoicemailToolDTO",
        Unset,
    ] = UNSET
    provider_details: Union[
        "FunctionToolProviderDetails", "GhlToolProviderDetails", "MakeToolProviderDetails", Unset
    ] = UNSET
    metadata: Union[Unset, "ToolTemplateMetadata"] = UNSET
    visibility: Union[Unset, UpdateToolTemplateDTOVisibility] = UNSET
    name: Union[Unset, str] = UNSET
    provider: Union[Unset, UpdateToolTemplateDTOProvider] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_dtmf_tool_dto import CreateDtmfToolDTO
        from ..models.create_end_call_tool_dto import CreateEndCallToolDTO
        from ..models.create_function_tool_dto import CreateFunctionToolDTO
        from ..models.create_ghl_tool_dto import CreateGhlToolDTO
        from ..models.create_make_tool_dto import CreateMakeToolDTO
        from ..models.create_voicemail_tool_dto import CreateVoicemailToolDTO
        from ..models.ghl_tool_provider_details import GhlToolProviderDetails
        from ..models.make_tool_provider_details import MakeToolProviderDetails

        type_ = self.type_.value

        details: Union[Unset, dict[str, Any]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, CreateDtmfToolDTO):
            details = self.details.to_dict()
        elif isinstance(self.details, CreateEndCallToolDTO):
            details = self.details.to_dict()
        elif isinstance(self.details, CreateVoicemailToolDTO):
            details = self.details.to_dict()
        elif isinstance(self.details, CreateFunctionToolDTO):
            details = self.details.to_dict()
        elif isinstance(self.details, CreateGhlToolDTO):
            details = self.details.to_dict()
        elif isinstance(self.details, CreateMakeToolDTO):
            details = self.details.to_dict()
        else:
            details = self.details.to_dict()

        provider_details: Union[Unset, dict[str, Any]]
        if isinstance(self.provider_details, Unset):
            provider_details = UNSET
        elif isinstance(self.provider_details, MakeToolProviderDetails):
            provider_details = self.provider_details.to_dict()
        elif isinstance(self.provider_details, GhlToolProviderDetails):
            provider_details = self.provider_details.to_dict()
        else:
            provider_details = self.provider_details.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        name = self.name

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if provider_details is not UNSET:
            field_dict["providerDetails"] = provider_details
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if name is not UNSET:
            field_dict["name"] = name
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_dtmf_tool_dto import CreateDtmfToolDTO
        from ..models.create_end_call_tool_dto import CreateEndCallToolDTO
        from ..models.create_function_tool_dto import CreateFunctionToolDTO
        from ..models.create_ghl_tool_dto import CreateGhlToolDTO
        from ..models.create_make_tool_dto import CreateMakeToolDTO
        from ..models.create_transfer_call_tool_dto import CreateTransferCallToolDTO
        from ..models.create_voicemail_tool_dto import CreateVoicemailToolDTO
        from ..models.function_tool_provider_details import FunctionToolProviderDetails
        from ..models.ghl_tool_provider_details import GhlToolProviderDetails
        from ..models.make_tool_provider_details import MakeToolProviderDetails
        from ..models.tool_template_metadata import ToolTemplateMetadata

        d = src_dict.copy()
        type_ = UpdateToolTemplateDTOType(d.pop("type"))

        def _parse_details(
            data: object,
        ) -> Union[
            "CreateDtmfToolDTO",
            "CreateEndCallToolDTO",
            "CreateFunctionToolDTO",
            "CreateGhlToolDTO",
            "CreateMakeToolDTO",
            "CreateTransferCallToolDTO",
            "CreateVoicemailToolDTO",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = CreateDtmfToolDTO.from_dict(data)

                return details_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_1 = CreateEndCallToolDTO.from_dict(data)

                return details_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_2 = CreateVoicemailToolDTO.from_dict(data)

                return details_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_3 = CreateFunctionToolDTO.from_dict(data)

                return details_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_4 = CreateGhlToolDTO.from_dict(data)

                return details_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_5 = CreateMakeToolDTO.from_dict(data)

                return details_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            details_type_6 = CreateTransferCallToolDTO.from_dict(data)

            return details_type_6

        details = _parse_details(d.pop("details", UNSET))

        def _parse_provider_details(
            data: object,
        ) -> Union["FunctionToolProviderDetails", "GhlToolProviderDetails", "MakeToolProviderDetails", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_details_type_0 = MakeToolProviderDetails.from_dict(data)

                return provider_details_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_details_type_1 = GhlToolProviderDetails.from_dict(data)

                return provider_details_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            provider_details_type_2 = FunctionToolProviderDetails.from_dict(data)

            return provider_details_type_2

        provider_details = _parse_provider_details(d.pop("providerDetails", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ToolTemplateMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ToolTemplateMetadata.from_dict(_metadata)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, UpdateToolTemplateDTOVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = UpdateToolTemplateDTOVisibility(_visibility)

        name = d.pop("name", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, UpdateToolTemplateDTOProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = UpdateToolTemplateDTOProvider(_provider)

        update_tool_template_dto = cls(
            type_=type_,
            details=details,
            provider_details=provider_details,
            metadata=metadata,
            visibility=visibility,
            name=name,
            provider=provider,
        )

        update_tool_template_dto.additional_properties = d
        return update_tool_template_dto

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

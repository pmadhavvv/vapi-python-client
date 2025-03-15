from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_request_method import ApiRequestMethod
from ..models.api_request_mode import ApiRequestMode
from ..models.api_request_type import ApiRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_request_metadata import ApiRequestMetadata
    from ..models.hook import Hook
    from ..models.json_schema import JsonSchema


T = TypeVar("T", bound="ApiRequest")


@_attrs_define
class ApiRequest:
    """
    Attributes:
        type_ (ApiRequestType):
        method (ApiRequestMethod):
        url (str): Api endpoint to send requests to.
        mode (ApiRequestMode): This is the mode of the Api Request.
            We only support BLOCKING and BACKGROUND for now.
        name (str):
        headers (Union[Unset, JsonSchema]):
        body (Union[Unset, JsonSchema]):
        hooks (Union[Unset, list['Hook']]): This is a list of hooks for a task.
            Each hook is a list of tasks to run on a trigger (such as on start, on failure, etc).
            Only Say is supported for now.
        output (Union[Unset, JsonSchema]):
        metadata (Union[Unset, ApiRequestMetadata]): This is for metadata you want to store on the task.
    """

    type_: ApiRequestType
    method: ApiRequestMethod
    url: str
    mode: ApiRequestMode
    name: str
    headers: Union[Unset, "JsonSchema"] = UNSET
    body: Union[Unset, "JsonSchema"] = UNSET
    hooks: Union[Unset, list["Hook"]] = UNSET
    output: Union[Unset, "JsonSchema"] = UNSET
    metadata: Union[Unset, "ApiRequestMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        method = self.method.value

        url = self.url

        mode = self.mode.value

        name = self.name

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        hooks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = []
            for hooks_item_data in self.hooks:
                hooks_item = hooks_item_data.to_dict()
                hooks.append(hooks_item)

        output: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "method": method,
                "url": url,
                "mode": mode,
                "name": name,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body is not UNSET:
            field_dict["body"] = body
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if output is not UNSET:
            field_dict["output"] = output
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.api_request_metadata import ApiRequestMetadata
        from ..models.hook import Hook
        from ..models.json_schema import JsonSchema

        d = src_dict.copy()
        type_ = ApiRequestType(d.pop("type"))

        method = ApiRequestMethod(d.pop("method"))

        url = d.pop("url")

        mode = ApiRequestMode(d.pop("mode"))

        name = d.pop("name")

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, JsonSchema]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = JsonSchema.from_dict(_headers)

        _body = d.pop("body", UNSET)
        body: Union[Unset, JsonSchema]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = JsonSchema.from_dict(_body)

        hooks = []
        _hooks = d.pop("hooks", UNSET)
        for hooks_item_data in _hooks or []:
            hooks_item = Hook.from_dict(hooks_item_data)

            hooks.append(hooks_item)

        _output = d.pop("output", UNSET)
        output: Union[Unset, JsonSchema]
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = JsonSchema.from_dict(_output)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ApiRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ApiRequestMetadata.from_dict(_metadata)

        api_request = cls(
            type_=type_,
            method=method,
            url=url,
            mode=mode,
            name=name,
            headers=headers,
            body=body,
            hooks=hooks,
            output=output,
            metadata=metadata,
        )

        api_request.additional_properties = d
        return api_request

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

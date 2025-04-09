from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenRestrictions")


@_attrs_define
class TokenRestrictions:
    """
    Attributes:
        enabled (Union[Unset, bool]): This determines whether the token is enabled or disabled. Default is true, it's
            enabled.
        allowed_origins (Union[Unset, list[str]]): This determines the allowed origins for this token. Validates the
            `Origin` header. Default is any origin.

            Only relevant for `public` tokens.
        allowed_assistant_ids (Union[Unset, list[str]]): This determines which assistantIds can be used when creating a
            call. Default is any assistantId.

            Only relevant for `public` tokens.
        allow_transient_assistant (Union[Unset, bool]): This determines whether transient assistants can be used when
            creating a call. Default is true.

            If `allowedAssistantIds` is provided, this is automatically false.

            Only relevant for `public` tokens.
    """

    enabled: Union[Unset, bool] = UNSET
    allowed_origins: Union[Unset, list[str]] = UNSET
    allowed_assistant_ids: Union[Unset, list[str]] = UNSET
    allow_transient_assistant: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        allowed_origins: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_origins, Unset):
            allowed_origins = self.allowed_origins

        allowed_assistant_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_assistant_ids, Unset):
            allowed_assistant_ids = self.allowed_assistant_ids

        allow_transient_assistant = self.allow_transient_assistant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if allowed_origins is not UNSET:
            field_dict["allowedOrigins"] = allowed_origins
        if allowed_assistant_ids is not UNSET:
            field_dict["allowedAssistantIds"] = allowed_assistant_ids
        if allow_transient_assistant is not UNSET:
            field_dict["allowTransientAssistant"] = allow_transient_assistant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        allowed_origins = cast(list[str], d.pop("allowedOrigins", UNSET))

        allowed_assistant_ids = cast(list[str], d.pop("allowedAssistantIds", UNSET))

        allow_transient_assistant = d.pop("allowTransientAssistant", UNSET)

        token_restrictions = cls(
            enabled=enabled,
            allowed_origins=allowed_origins,
            allowed_assistant_ids=allowed_assistant_ids,
            allow_transient_assistant=allow_transient_assistant,
        )

        token_restrictions.additional_properties = d
        return token_restrictions

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

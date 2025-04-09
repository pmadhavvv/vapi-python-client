from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan


T = TypeVar("T", bound="UpdateCustomLLMCredentialDTO")


@_attrs_define
class UpdateCustomLLMCredentialDTO:
    """
    Attributes:
        api_key (Union[Unset, str]): This is not returned in the API.
        authentication_plan (Union[Unset, OAuth2AuthenticationPlan]):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    api_key: Union[Unset, str] = UNSET
    authentication_plan: Union[Unset, "OAuth2AuthenticationPlan"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        authentication_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.authentication_plan, Unset):
            authentication_plan = self.authentication_plan.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if authentication_plan is not UNSET:
            field_dict["authenticationPlan"] = authentication_plan
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan

        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        _authentication_plan = d.pop("authenticationPlan", UNSET)
        authentication_plan: Union[Unset, OAuth2AuthenticationPlan]
        if isinstance(_authentication_plan, Unset):
            authentication_plan = UNSET
        else:
            authentication_plan = OAuth2AuthenticationPlan.from_dict(_authentication_plan)

        name = d.pop("name", UNSET)

        update_custom_llm_credential_dto = cls(
            api_key=api_key,
            authentication_plan=authentication_plan,
            name=name,
        )

        update_custom_llm_credential_dto.additional_properties = d
        return update_custom_llm_credential_dto

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

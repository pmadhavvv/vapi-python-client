from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_webhook_credential_dto_provider import CreateWebhookCredentialDTOProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan


T = TypeVar("T", bound="CreateWebhookCredentialDTO")


@_attrs_define
class CreateWebhookCredentialDTO:
    """
    Attributes:
        provider (CreateWebhookCredentialDTOProvider):
        authentication_plan (OAuth2AuthenticationPlan):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateWebhookCredentialDTOProvider
    authentication_plan: "OAuth2AuthenticationPlan"
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        authentication_plan = self.authentication_plan.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "authenticationPlan": authentication_plan,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan

        d = src_dict.copy()
        provider = CreateWebhookCredentialDTOProvider(d.pop("provider"))

        authentication_plan = OAuth2AuthenticationPlan.from_dict(d.pop("authenticationPlan"))

        name = d.pop("name", UNSET)

        create_webhook_credential_dto = cls(
            provider=provider,
            authentication_plan=authentication_plan,
            name=name,
        )

        create_webhook_credential_dto.additional_properties = d
        return create_webhook_credential_dto

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

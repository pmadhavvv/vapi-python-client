from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_voice_library_dto_providers import SyncVoiceLibraryDTOProviders
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncVoiceLibraryDTO")


@_attrs_define
class SyncVoiceLibraryDTO:
    """
    Attributes:
        providers (Union[Unset, SyncVoiceLibraryDTOProviders]): List of providers you want to sync.
    """

    providers: Union[Unset, SyncVoiceLibraryDTOProviders] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        providers: Union[Unset, str] = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _providers = d.pop("providers", UNSET)
        providers: Union[Unset, SyncVoiceLibraryDTOProviders]
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = SyncVoiceLibraryDTOProviders(_providers)

        sync_voice_library_dto = cls(
            providers=providers,
        )

        sync_voice_library_dto.additional_properties = d
        return sync_voice_library_dto

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

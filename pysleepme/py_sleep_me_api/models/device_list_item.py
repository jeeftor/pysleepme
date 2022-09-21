from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceListItem")


@attr.s(auto_attribs=True)
class DeviceListItem:
    """
    Attributes:
        id (Union[Unset, str]): The ID of the device. Example: zx-c4ggl2522wj5t2265jg.
        name (Union[Unset, str]): The name of the device. Example: My Dock Pro.
        attachments (Union[Unset, List[str]]): The attachments for the given device.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    attachments: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id
        name = self.name
        attachments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        device_list_item = cls(
            id=id,
            name=name,
            attachments=attachments,
        )

        device_list_item.additional_properties = d
        return device_list_item

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

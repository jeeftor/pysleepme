from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusAbout")


@attr.s(auto_attribs=True)
class StatusAbout:
    """
    Attributes:
        firmware_version (Union[Unset, str]):  Example: 1.0.
        ip_address (Union[Unset, str]):  Example: 3.211.177.219.
        lan_address (Union[Unset, str]):  Example: 192.168.1.1.
        mac_address (Union[Unset, str]):  Example: 89:3F:28:3A:C3:A9.
        model (Union[Unset, str]):  Example: DP999NA.
        serial_number (Union[Unset, str]):  Example: 1234567890.
    """

    firmware_version: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    lan_address: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        firmware_version = self.firmware_version
        ip_address = self.ip_address
        lan_address = self.lan_address
        mac_address = self.mac_address
        model = self.model
        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firmware_version is not UNSET:
            field_dict["firmware_version"] = firmware_version
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if lan_address is not UNSET:
            field_dict["lan_address"] = lan_address
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if model is not UNSET:
            field_dict["model"] = model
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        firmware_version = d.pop("firmware_version", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        lan_address = d.pop("lan_address", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        model = d.pop("model", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        status_about = cls(
            firmware_version=firmware_version,
            ip_address=ip_address,
            lan_address=lan_address,
            mac_address=mac_address,
            model=model,
            serial_number=serial_number,
        )

        status_about.additional_properties = d
        return status_about

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

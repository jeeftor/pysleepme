from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusStatus")


@attr.s(auto_attribs=True)
class StatusStatus:
    """
    Attributes:
        is_connected (Union[Unset, bool]):  Example: True.
        is_water_low (Union[Unset, bool]):
        water_level (Union[Unset, float]):  Example: 100.
        water_temperature_f (Union[Unset, float]):  Example: 91.
        water_temperature_c (Union[Unset, float]):  Example: 32.5.
    """

    is_connected: Union[Unset, bool] = UNSET
    is_water_low: Union[Unset, bool] = UNSET
    water_level: Union[Unset, float] = UNSET
    water_temperature_f: Union[Unset, float] = UNSET
    water_temperature_c: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_connected = self.is_connected
        is_water_low = self.is_water_low
        water_level = self.water_level
        water_temperature_f = self.water_temperature_f
        water_temperature_c = self.water_temperature_c

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_connected is not UNSET:
            field_dict["is_connected"] = is_connected
        if is_water_low is not UNSET:
            field_dict["is_water_low"] = is_water_low
        if water_level is not UNSET:
            field_dict["water_level"] = water_level
        if water_temperature_f is not UNSET:
            field_dict["water_temperature_f"] = water_temperature_f
        if water_temperature_c is not UNSET:
            field_dict["water_temperature_c"] = water_temperature_c

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        is_connected = d.pop("is_connected", UNSET)

        is_water_low = d.pop("is_water_low", UNSET)

        water_level = d.pop("water_level", UNSET)

        water_temperature_f = d.pop("water_temperature_f", UNSET)

        water_temperature_c = d.pop("water_temperature_c", UNSET)

        status_status = cls(
            is_connected=is_connected,
            is_water_low=is_water_low,
            water_level=water_level,
            water_temperature_f=water_temperature_f,
            water_temperature_c=water_temperature_c,
        )

        status_status.additional_properties = d
        return status_status

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

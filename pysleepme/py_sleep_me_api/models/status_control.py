from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusControl")


@attr.s(auto_attribs=True)
class StatusControl:
    """
    Attributes:
        brightness_level (Union[Unset, float]):  Example: 100.
        display_temperature_unit (Union[Unset, str]):  Example: f.
        set_temperature_c (Union[Unset, float]):  Example: 35.
        set_temperature_f (Union[Unset, float]):  Example: 95.
        thermal_control_status (Union[Unset, str]):  Example: active.
        time_zone (Union[Unset, str]):  Example: America/New_York.
    """

    brightness_level: Union[Unset, float] = UNSET
    display_temperature_unit: Union[Unset, str] = UNSET
    set_temperature_c: Union[Unset, float] = UNSET
    set_temperature_f: Union[Unset, float] = UNSET
    thermal_control_status: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brightness_level = self.brightness_level
        display_temperature_unit = self.display_temperature_unit
        set_temperature_c = self.set_temperature_c
        set_temperature_f = self.set_temperature_f
        thermal_control_status = self.thermal_control_status
        time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brightness_level is not UNSET:
            field_dict["brightness_level"] = brightness_level
        if display_temperature_unit is not UNSET:
            field_dict["display_temperature_unit"] = display_temperature_unit
        if set_temperature_c is not UNSET:
            field_dict["set_temperature_c"] = set_temperature_c
        if set_temperature_f is not UNSET:
            field_dict["set_temperature_f"] = set_temperature_f
        if thermal_control_status is not UNSET:
            field_dict["thermal_control_status"] = thermal_control_status
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        brightness_level = d.pop("brightness_level", UNSET)

        display_temperature_unit = d.pop("display_temperature_unit", UNSET)

        set_temperature_c = d.pop("set_temperature_c", UNSET)

        set_temperature_f = d.pop("set_temperature_f", UNSET)

        thermal_control_status = d.pop("thermal_control_status", UNSET)

        time_zone = d.pop("time_zone", UNSET)

        status_control = cls(
            brightness_level=brightness_level,
            display_temperature_unit=display_temperature_unit,
            set_temperature_c=set_temperature_c,
            set_temperature_f=set_temperature_f,
            thermal_control_status=thermal_control_status,
            time_zone=time_zone,
        )

        status_control.additional_properties = d
        return status_control

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

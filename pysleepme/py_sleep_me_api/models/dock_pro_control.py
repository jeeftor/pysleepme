from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dock_pro_control_display_temperature_unit import DockProControlDisplayTemperatureUnit
from ..models.dock_pro_control_thermal_control_status import DockProControlThermalControlStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DockProControl")


@attr.s(auto_attribs=True)
class DockProControl:
    """
    Attributes:
        thermal_control_status (Union[Unset, DockProControlThermalControlStatus]):  Example: active.
        set_temperature_f (Union[Unset, float]):  Example: 72.0.
        set_temperature_c (Union[Unset, float]):  Example: 20.5.
        display_temperature_unit (Union[Unset, DockProControlDisplayTemperatureUnit]):  Example: f.
        time_zone (Union[Unset, str]):  Example: America/New_York.
    """

    thermal_control_status: Union[Unset, DockProControlThermalControlStatus] = UNSET
    set_temperature_f: Union[Unset, float] = UNSET
    set_temperature_c: Union[Unset, float] = UNSET
    display_temperature_unit: Union[Unset, DockProControlDisplayTemperatureUnit] = UNSET
    time_zone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thermal_control_status: Union[Unset, str] = UNSET
        if not isinstance(self.thermal_control_status, Unset):
            thermal_control_status = self.thermal_control_status.value

        set_temperature_f = self.set_temperature_f
        set_temperature_c = self.set_temperature_c
        display_temperature_unit: Union[Unset, str] = UNSET
        if not isinstance(self.display_temperature_unit, Unset):
            display_temperature_unit = self.display_temperature_unit.value

        time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thermal_control_status is not UNSET:
            field_dict["thermal_control_status"] = thermal_control_status
        if set_temperature_f is not UNSET:
            field_dict["set_temperature_f"] = set_temperature_f
        if set_temperature_c is not UNSET:
            field_dict["set_temperature_c"] = set_temperature_c
        if display_temperature_unit is not UNSET:
            field_dict["display_temperature_unit"] = display_temperature_unit
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _thermal_control_status = d.pop("thermal_control_status", UNSET)
        thermal_control_status: Union[Unset, DockProControlThermalControlStatus]
        if isinstance(_thermal_control_status, Unset):
            thermal_control_status = UNSET
        else:
            thermal_control_status = DockProControlThermalControlStatus(_thermal_control_status)

        set_temperature_f = d.pop("set_temperature_f", UNSET)

        set_temperature_c = d.pop("set_temperature_c", UNSET)

        _display_temperature_unit = d.pop("display_temperature_unit", UNSET)
        display_temperature_unit: Union[Unset, DockProControlDisplayTemperatureUnit]
        if isinstance(_display_temperature_unit, Unset):
            display_temperature_unit = UNSET
        else:
            display_temperature_unit = DockProControlDisplayTemperatureUnit(_display_temperature_unit)

        time_zone = d.pop("time_zone", UNSET)

        dock_pro_control = cls(
            thermal_control_status=thermal_control_status,
            set_temperature_f=set_temperature_f,
            set_temperature_c=set_temperature_c,
            display_temperature_unit=display_temperature_unit,
            time_zone=time_zone,
        )

        dock_pro_control.additional_properties = d
        return dock_pro_control

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

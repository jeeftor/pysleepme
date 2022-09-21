from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.status_about import StatusAbout
from ..models.status_control import StatusControl
from ..models.status_status import StatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@attr.s(auto_attribs=True)
class Status:
    """
    Attributes:
        about (Union[Unset, StatusAbout]):
        control (Union[Unset, StatusControl]):
        status (Union[Unset, StatusStatus]):
    """

    about: Union[Unset, StatusAbout] = UNSET
    control: Union[Unset, StatusControl] = UNSET
    status: Union[Unset, StatusStatus] = UNSET
    additional_properties: dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        about: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.about, Unset):
            about = self.about.to_dict()

        control: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.control, Unset):
            control = self.control.to_dict()

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if about is not UNSET:
            field_dict["about"] = about
        if control is not UNSET:
            field_dict["control"] = control
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _about = d.pop("about", UNSET)
        about: Union[Unset, StatusAbout]
        if isinstance(_about, Unset):
            about = UNSET
        else:
            about = StatusAbout.from_dict(_about)

        _control = d.pop("control", UNSET)
        control: Union[Unset, StatusControl]
        if isinstance(_control, Unset):
            control = UNSET
        else:
            control = StatusControl.from_dict(_control)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusStatus.from_dict(_status)

        status = cls(
            about=about,
            control=control,
            status=status,
        )

        status.additional_properties = d
        return status

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

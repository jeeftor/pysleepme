from enum import Enum


class DockProControlThermalControlStatus(str, Enum):
    ACTIVE = "active"
    STANDBY = "standby"

    def __str__(self) -> str:
        return str(self.value)

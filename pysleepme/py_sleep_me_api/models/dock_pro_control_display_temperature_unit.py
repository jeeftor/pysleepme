from enum import Enum


class DockProControlDisplayTemperatureUnit(str, Enum):
    C = "c"
    F = "f"

    def __str__(self) -> str:
        return str(self.value)

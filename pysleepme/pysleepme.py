"""Main module."""
from __future__ import annotations

import logging

from pysleepme.exceptions import get_exception_by_status
from pysleepme.py_sleep_me_api import AuthenticatedClient
from pysleepme.py_sleep_me_api.api.device_control import get_devices
from pysleepme.py_sleep_me_api.models import DeviceListItem

from .const import BASE_URL
from .py_sleep_me_api.types import Response

_LOGGER = logging.getLogger("__package__")


class PySleepMe:
    """Class definition."""

    def __init__(self, api_token: str) -> None:
        """Initialize Class."""
        self.client = AuthenticatedClient(base_url=BASE_URL, token=api_token, verify_ssl=False)

    def get_devices_sync(self) -> list[DeviceListItem]:
        """Make a sync query for devices."""
        devices = get_devices.sync(client=self.client)
        response: Response[list[DeviceListItem]] = get_devices.sync_detailed(client=self.client)
        if response.status_code == 200:
            devices = response.parsed
            return devices or []
        else:
            raise get_exception_by_status(response.status_code)

    async def get_devices_async(self) -> list[DeviceListItem]:
        """Async query for devices."""
        devices = await get_devices.asyncio(client=self.client)
        response: Response[list[DeviceListItem]] = await get_devices.asyncio_detailed(client=self.client)
        if response.status_code == 200:
            devices = response.parsed
            return devices or []
        else:
            raise get_exception_by_status(response.status_code)

    # def get_device_by_id_sync(self, id: str):
    #     """Query for a device."""
    #     device: Status = get_devices_device_id.sync(client=self.client)
    #     response: Response[Status] = get_devices_device_id.sync_detailed(client=self.client)

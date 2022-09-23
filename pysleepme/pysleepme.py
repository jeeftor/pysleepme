"""Main module."""
from __future__ import annotations

import logging

from pysleepme.py_sleep_me_api import AuthenticatedClient
from pysleepme.py_sleep_me_api.api.device_control import get_devices
from pysleepme.py_sleep_me_api.models import DeviceListItem

from .const import BASE_URL

_LOGGER = logging.getLogger("__package__")


class PySleepMe:
    """Class definition."""

    def __init__(self, api_token: str) -> None:
        """Initialize Class."""
        self.client = AuthenticatedClient(base_url=BASE_URL, token=api_token, verify_ssl=False)

    def get_devices_sync(self) -> list[DeviceListItem]:
        """Make a sync query for devices."""
        devices = get_devices.sync(client=self.client)
        # response: Response[list[DeviceListItem]] = get_devices.sync_detailed(client=self.client)
        return devices or []

    async def get_devices_async(self) -> list[DeviceListItem] | None:
        """Async query for devices."""
        devices = await get_devices.asyncio(client=self.client)
        return devices or []

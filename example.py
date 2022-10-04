"""Example of use."""
from __future__ import annotations

import asyncio
import os

from pysleepme.py_sleep_me_api.models import DeviceListItem
from pysleepme.pysleepme import PySleepMe

token: str | None = os.getenv('API_TOKEN')

if token is None:
    print("Make sure to have the environment variable API_TOKEN set")
    exit(1)


psm = PySleepMe(api_token=token)


async def async_main() -> None:
    """Async main function."""
    d = await psm.get_devices_async()
    print(d)


def sync_main() -> None:
    """Sync main function."""
    d: list[DeviceListItem] = psm.get_devices_sync()
    info = psm.get_device_by_id_sync(d[0].id)
    print(info)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())

    sync_main()

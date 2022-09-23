"""Example of use."""
from __future__ import annotations

import asyncio
import os

from pysleepme.pysleepme import PySleepMe

token: str | None = os.getenv('API_TOKEN')

if token is None:
    print("Make sure to have the environment variable API_TOKEN set")
    exit(1)


psm = PySleepMe(api_token=token)


async def async_main() -> None:
    """Async main function."""
    await psm.get_devices_async()


def sync_main() -> None:
    """Sync main function."""
    psm.get_devices_sync()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())

    sync_main()

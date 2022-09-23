"""Test fixtures."""
import json
from collections.abc import Generator

import pytest
import respx
from httpx import Response

from pysleepme.const import BASE_URL, ENDPOINT_DEVICES

DEVICES_RESPONSE = '''[
    {
        "id": "zx-cagh25ahjfawkfawhg",
        "name": "My Dock Pro",
        "attachments": [
            "CHILIPAD_PRO"
        ]
    },
    {
        "id": "zx-wagagj21qk222j25525",
        "name": "Another Dock Pro",
        "attachments": [
            "CHILIPAD_PRO"
        ]
    }
]'''
SINGLE_DEVICE_RESPONSE = '''{
    "about": {
        "firmware_version": "5.15",
        "ip_address": "25.26.873.23",
        "lan_address": "192.168.0.131",
        "mac_address": "b5:56:12:67:jg:w2",
        "model": "DP999NA",
        "serial_number": "6236265923682376276"
    },
    "control": {
        "brightness_level": 100,
        "display_temperature_unit": "f",
        "set_temperature_c": 23.5,
        "set_temperature_f": 74,
        "thermal_control_status": "active",
        "time_zone": "America/New_York"
    },
    "status": {
        "is_connected": true,
        "is_water_low": false,
        "water_level": 100,
        "water_temperature_f": 74,
        "water_temperature_c": 23.5
    }
}'''


@pytest.fixture()
def mock_get_devices_with_error(status_code: int) -> Generator:
    """Parameterizable fixture."""
    with respx.mock(base_url=BASE_URL, assert_all_called=False) as respx_mock:
        devices_route = respx_mock.get(f"/{ENDPOINT_DEVICES}")
        devices_route.return_value = Response(status_code)
        yield respx_mock


@pytest.fixture()
def mock_get_devices() -> Generator:
    """Test fixture for devices endpoint."""
    with respx.mock(base_url=BASE_URL, assert_all_called=False) as respx_mock:
        devices_route = respx_mock.get(f"/{ENDPOINT_DEVICES}")
        devices_route.return_value = Response(200, json=json.loads(DEVICES_RESPONSE))
        yield respx_mock

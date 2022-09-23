#!/usr/bin/env python
"""Tests for `pysleepme` package."""
import json

from httpx import Response

from pysleepme.const import GET_DEVICES_URL
from pysleepme.pysleepme import PySleepMe

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


# @pytest.fixture
# def response() -> None:
#     """Sample pytest fixture.
#
#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response) -> None:
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string
#     del response


# @pytest.fixture(autouse=True)
# def httpx_mock_devices():


def test_devices_sync(respx_mock) -> None:  # type: ignore
    """Test the sync get devices call."""
    respx_mock.get(GET_DEVICES_URL).mock(return_value=Response(200, json=json.loads(DEVICES_RESPONSE)))
    TOKEN = "FAKE_TOKEN"
    psm = PySleepMe(api_token=TOKEN)
    devices = psm.get_devices_sync()
    assert len(devices) == 2
    assert devices[1].id == 'zx-wagagj21qk222j25525'

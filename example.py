"""Example of use."""
import os

from pysleepme.pysleepme import PySleepMe

token: str = os.getenv('API_TOKEN') or ""

psm = PySleepMe(api_token=token)

psm.get_devices_sync()

import unittest
from datetime import date

from battery.nubbin import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2021-08-21")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-09-11")
        last_service_date = date.fromisoformat("2020-06-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
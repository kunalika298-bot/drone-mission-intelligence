
import unittest

from mission_validator import validate_mission


class TestMissionValidator(unittest.TestCase):

    def test_valid_mission(self):
        mission = {
            "battery": 80,
            "wind_speed": 15,
            "gps_status": True,
        }
        result = validate_mission(mission)
        self.assertTrue(result["valid"])
        self.assertEqual(result["errors"], [])

    def test_missing_field(self):
        mission = {
            "battery": 80,
            "gps_status": True,
        }
        result = validate_mission(mission)
        self.assertFalse(result["valid"])
        self.assertTrue(result["errors"])

    def test_battery_out_of_range(self):
        mission = {
            "battery": 120,
            "wind_speed": 15,
            "gps_status": True,
        }
        result = validate_mission(mission)
        self.assertFalse(result["valid"])

    def test_negative_wind_speed(self):
        mission = {
            "battery": 80,
            "wind_speed": -5,
            "gps_status": True,
        }
        result = validate_mission(mission)
        self.assertFalse(result["valid"])

    def test_invalid_gps_type(self):
        mission = {
            "battery": 80,
            "wind_speed": 15,
            "gps_status": "yes",
        }
        result = validate_mission(mission)
        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

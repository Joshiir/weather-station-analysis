import weather_station
import unittest


json_data = {
    23: [
            {
                " Timestamp": "Feb 2011",
                " Value": "159.6"
            },
            {
                "Timestamp": "Mar 2011",
                "Value": "78.6"
            }
        ]
    }

ws = weather_station.WeatherStation()


class TestWeatherStation(unittest.TestCase):
    def test_str_to_float(self):
        """
        Tests the function to check the string input
        is changed to a float.
        """
        self.assertEqual(weather_station.str_to_float("125"), 125.0)

    def test_str_to_int(self):
        """
        Tests the function to check the string input
        is changed to an integer.
        """
        self.assertEqual(weather_station.str_to_int("125"), 125)

    def test_from_json(self):
        """
        Tests the function for its return
        value being True.
        """
        self.assertEqual(ws.from_json(json_data), True)

    def test_years(self):
        """
        The function should return each
        year only once.
        """
        self.assertEqual(ws.years(json_data))

    def test_maximum_per_year(self):
        """
        The function should return the
        max value per year
        """
        self.assertEqual(ws.maximum_per_year(json_data))


if __name__ == "__main__":
    unittest.main()

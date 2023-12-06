import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from Lab7.dogs import *

class TestDisplayDogApi(unittest.TestCase):
    @patch('requests.get')
    def test_get_all_breeds(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": {"breed1": {}, "breed2": {}}}
        mock_requests_get.return_value = mock_response

        breeds = DisplayDogApi.get_all_breeds()

        self.assertEqual(list(breeds), ["breed1", "breed2"])

class TestConsoleInterface(unittest.TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_invalid_display_format(self, mock_input):
        with self.assertRaises((ValueError, StopIteration)):
            choose_display_format()

if __name__ == '__main__':
    unittest.main()

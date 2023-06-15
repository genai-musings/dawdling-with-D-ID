import unittest

from unittest.mock import patch, MagicMock

import logging

import os

import requests

import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from didAnimations import Animations


class TestAnimations(unittest.TestCase):
    def setUp(self):
        self.api_key = "dummy_api_key"
        self.animations = Animations(api_key=self.api_key)

    # Test case to validate the get_all_animations method with a successful response
    @patch("didAnimations.requests.get")
    def test_get_all_animations_success(self, mock_get):
        # Set up mock return value
        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = ["animation1", "animation2"]
        mock_get.return_value = response_mock

        # Call the method under test
        result = self.animations.get_all_animations()

        # Assertions
        mock_get.assert_called_once_with(
            "https://api.d-id.com/animations",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json",
            },
            timeout=None,
        )
        self.assertEqual(result, ["animation1", "animation2"])

    # Test case to validate the get_all_animations method when an exception occurs
    @patch("didAnimations.requests.get")
    @patch("didAnimations.logging.error")
    def test_get_all_animations_error(self, mock_logging_error, mock_get):
        # Set up mock exception
        exception_mock = requests.exceptions.RequestException("Mock exception")
        mock_get.side_effect = exception_mock

        # Call the method under test and expect an exception to be raised
        with self.assertRaises(requests.exceptions.RequestException):
            self.animations.get_all_animations()

        # Assertions
        mock_logging_error.assert_called_once_with(
            f"Error getting animations: {exception_mock}"
        )


if __name__ == "__main__":
    unittest.main()

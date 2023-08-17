import unittest

from unittest.mock import patch, MagicMock

import logging

import os

import requests

import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from didTalks import Talks


class TestTalks(unittest.TestCase):
    def setUp(self):
        self.api_key = "dummy_api_key"
        self.talks = Talks(api_key=self.api_key)

    # Test case to validate the get_all_talks method with a successful response
    @patch("didTalks.requests.get")
    def test_get_all_talks_success(self, mock_get):
        # Set up mock return value
        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = ["talk1", "talk2"]
        mock_get.return_value = response_mock

        # Call the method under test
        result = self.talks.get_all_talks()

        # Assertions
        mock_get.assert_called_once_with(
            "https://api.d-id.com/talks",
            headers={
                "Authorization": f"Basic {self.api_key}",
                "Accept": "application/json",
            },
            timeout=30,
        )
        self.assertEqual(result, ["talk1", "talk2"])

    # Test case to validate the get_all_talks method when an exception occurs
    @patch("didTalks.requests.get")
    @patch("didTalks.logging.error")
    def test_get_all_talks_error(self, mock_logging_error, mock_get):
        # Set up mock exception
        exception_mock = requests.exceptions.RequestException("Mock exception")
        mock_get.side_effect = exception_mock

        # Call the method under test and expect an exception to be raised
        with self.assertRaises(requests.exceptions.RequestException):
            self.talks.get_all_talks()

        # Assertions
        mock_logging_error.assert_called_once_with(
            f"Error getting talks: {exception_mock}"
        )

if __name__ == "__main__":
    unittest.main()

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

    # Test case to validate the create_talk method with a successful response
    @patch('requests.post')
    def test_create_talk_success(self, mock_post):
        # Create a mock response object for a successful API call
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "tlk_TestTalk123", "name": "Test Talk"}

        # Configure the mock post function to return the mock response
        mock_post.return_value = mock_response

        # Create an instance of the Talks class with the mock API key
        talks = Talks(self.api_key)

        # Call the create_talk method with test data
        talk_name = "Test Talk"
        talk_text = "This is a test talk."
        talk_image_url = "https://example.com/image.jpg"
        created_talk = talks.create_talk(talk_name, talk_text, talk_image_url)

        # Check if the response matches the expected result
        expected_result = {"id": "tlk_TestTalk123", "name": "Test Talk"}
        self.assertEqual(created_talk, expected_result)

    # Test case to validate the create_talk method when an exception occurs
    @patch('requests.post')
    def test_create_talk_failure(self, mock_post):
        # Create a mock response object for a failed API call
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("API request failed")

        # Configure the mock post function to return the mock response
        mock_post.return_value = mock_response

        # Create an instance of the Talks class with the mock API key
        talks = Talks(self.api_key)

        # Call the create_talk method with test data
        talk_name = "Test Talk"
        talk_text = "This is a test talk."
        talk_image_url = "https://example.com/image.jpg"

        # Verify that the method raises an exception for a failed API call
        with self.assertRaises(Exception):
            talks.create_talk(talk_name, talk_text, talk_image_url)

if __name__ == "__main__":
    unittest.main()

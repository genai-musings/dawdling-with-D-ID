import logging

import requests


class Talks:
    def __init__(self, api_key):
        """
        Initializes the Talks class with the provided API key.

        Args:
            api_key (str): The API key to authenticate the request.
        """
        self.api_key = api_key
        self.url = "https://api.d-id.com/talks"

    def get_all_talks(self):
        """
        Retrieves a list of talks via the D-ID Studio API.

        Returns:
            list: A list of talks if successful, None otherwise.
        """
        headers = {
            "Authorization": f"Basic {self.api_key}",
            "Accept": "application/json",
        }

        try:
            response = requests.get(self.url, headers=headers, timeout=None)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            talks = response.json()
            return talks
        except requests.exceptions.RequestException as e:
            # Log and raise an exception if an exception occurs during the API request
            logging.error(f"Error getting talks: {e}")
            raise

import logging

import requests


class Animations:
    def __init__(self, api_key):
        """
        Initializes the Animations class with the provided API key.

        Args:
            api_key (str): The API key to authenticate the request.
        """
        self.api_key = api_key
        self.url = "https://api.d-id.com/animations"

    def get_all_animations(self):
        """
        Retrieves a list of animations via the D-ID Studio API.

        Returns:
            list: A list of animations if successful, None otherwise.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }

        try:
            response = requests.get(self.url, headers=headers, timeout=None)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            animations = response.json()
            return animations
        except requests.exceptions.RequestException as e:
            # Log and raise an exception if an exception occurs during the API request
            logging.error(f"Error getting animations: {e}")
            raise

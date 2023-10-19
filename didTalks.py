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
        self.talksUrl = "https://api.d-id.com/talks"

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
            response = requests.get(self.talksUrl, headers=headers, timeout=30)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            talks = response.json()
            return talks
        except requests.exceptions.RequestException as e:
            # Log and raise an exception if an exception occurs during the API request
            logging.error(f"Error getting talks: {e}")
            raise

    def create_talk(self, talk_name, talk_text, talk_image_url):
        """
        Create a talk via the D-ID Studio API.

        Args:
            self (object): The instance of the class calling the function.
            talk_name (str): The name to give the talk to be generated.
            talk_text (str): The text content of the talk to be generated.
            talk_image_url (str): The URL of the image to be associated with the talk.

        Returns:
            list: Details on the talk created if successful, None otherwise.
        """
        headers = {
            "Authorization": f"Basic {self.api_key}",
            "Accept": "application/json",
        }

        payload = {
            "script": {
                "type": "text",
                "subtitles": "false",
                "provider": {
                    "type": "microsoft",
                    "voice_id": "en-US-GuyNeural"
                },
                "ssml": "false",
                "input": talk_text
            },
            "config": {
                "fluent": "false",
                "pad_audio": "0.0"
            },
            "persist": True,
            "name": talk_name,
            "source_url": talk_image_url
        }
        try:
            response = requests.post(self.talksUrl, json=payload, headers=headers, timeout=30)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            talk = response.json()
            return talk
        except requests.exceptions.RequestException as e:
            # Log and raise an exception if an exception occurs during the API request
            logging.error(f"Error creating talk: {e}")
            raise
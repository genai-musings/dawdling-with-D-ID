import logging
import json
import os
import sys

from didTalks import Talks

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Get the API key
api_key = os.environ.get("DID_KEY")
if not api_key:
    error_message = "DID_KEY environment variable is not set."
    logging.error(error_message)
    print(error_message)
    sys.exit(1)

# Create an instance of the D-ID Talks class
talks = Talks(api_key)

# Call the method to get the talks created
try:
    talks_list = talks.get_all_talks()

    # Process the JSON response
    # Extract and display some data from the JSON
    if talks_list is not None:
        # Access the talks list
        talks = talks_list['talks']

        # Iterate over the talks
        for talk in talks:
            user_data = json.loads(talk.get("user_data", "{}"))
            thumbnail_url = user_data.get("thumbnail_url")
            name = talk.get("name")
            print("Name: " + name + " Thumbnail Url:" + thumbnail_url)
    else:
        error_message = "Failed to get talks."
        logging.error(error_message)
        print(error_message)
except Exception as e:
    error_message = f"An error occurred: {str(e)}"
    logging.error(error_message)
    print(error_message)

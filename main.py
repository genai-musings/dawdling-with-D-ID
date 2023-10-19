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
talks_api = Talks(api_key)

def create_talk():
    """
    Function to create a talk.

    It first prompts the user for talk details and then sends a request to create the talk via the D-ID API.

    If the talk creation is successful, it prints the talk details.

    If any errors occur during the process, it logs an error message and prints the error.
    """
    try:
        print("\n\nEnter the Name to give the talk")
        print("Leave empty and press 'Return' to exit.\n\n")
        talk_name = str(input())

        if not talk_name:
            sys.exit()

        print("\n\nEnter the Text Content for the talk")
        print("Leave empty and press 'Return' to exit.\n\n")
        talk_text = str(input())

        if not talk_text:
            sys.exit()

        print("\n\nEnter the URL of the image to use for the talk")
        print("Leave empty and press 'Return' to exit.\n\n")
        talk_image_url = str(input())

        if not talk_image_url:
            sys.exit()

        talk = talks_api.create_talk(talk_name, talk_text, talk_image_url)
        # Note: You can comment the previous line and uncomment the following line to develop
        # and test without burning credits
        #talk = {'id': 'tlk_Testing123', 'created_at': '2023-10-19T08:38:11.699Z','created_by': 'auth0|testing123', 'status': 'created', 'object': 'talk'}
        if talk is not None:
            if 'id' not in talk:
                raise ValueError("The 'id' field is missing in the JSON data")
            print("Talk - Name: " + talk_name + " URL: https://studio.d-id.com/?video=" + talk.get("id"))
        else:
            error_message = "Failed to create talk."
            logging.error(error_message)
            print(error_message)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        logging.error(error_message)
        print(error_message)

def get_all_talks():
    """
    Function to get all talks.

    This function requests and retrieves a list of all talks via the D-ID API.

    If the request is successful, it prints the names and URLs of the talks returned.

    If any errors occur during the process, it logs an error message and prints the error.
    """
    try:
        talks_list = talks_api.get_all_talks()

        if talks_list is not None:
            talks = talks_list['talks']

            for talk in talks:
                user_data = json.loads(talk.get("user_data", "{}"))
                name = talk.get("name")
                talk_id = talk.get("id")
                print("Name: " + name + " Talk: https://studio.d-id.com/?video=" + talk_id)
        else:
            error_message = "Failed to get talks."
            logging.error(error_message)
            print(error_message)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        logging.error(error_message)
        print(error_message)

if __name__ == "__main__":
    while True:
        print("\n\nEnter:\n")
        print("1 - Get All Talks.")
        print("2 - Create a Talk.")
        print("\nAny other key to exit.\n")
        choice = input()
        if choice == "1":
            get_all_talks()
        elif choice == "2":
            create_talk()
        else:
            sys.exit(0)

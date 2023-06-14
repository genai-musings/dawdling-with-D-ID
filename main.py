import logging
import os
import sys

from didAnimations import Animations

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Get the API key
api_key = os.environ.get("DID_KEY")
if not api_key:
    error_message = "DID_KEY environment variable is not set."
    logging.error(error_message)
    print(error_message)
    sys.exit(1)

# Create an instance of the D-ID Animations class
animations = Animations(api_key)

# Call the method to get the animations created
try:
    animations_list = animations.get_all_animations()

    # Process the response
    if animations_list is not None:
        print("List of animations:")
        for animation in animations_list:
            print(animation)
    else:
        error_message = "Failed to get animations."
        logging.error(error_message)
        print(error_message)
except Exception as e:
    error_message = f"An error occurred: {str(e)}"
    logging.error(error_message)
    print(error_message)

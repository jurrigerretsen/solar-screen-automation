"""
This script loads environment variables and uses them to initialize a SomfyAPI object. 
It then logs in and checks the token status. Finally, it prints the status.
"""
import os
from somfy_api import SomfyAPI

try:
    SOMFY_URL = os.environ['SOMFY_URL']
    SOMFY_EMAIL = os.environ['SOMFY_EMAIL']
    SOMFY_PASSWORD = os.environ['SOMFY_PASSWORD']
    SOMFY_POD = os.environ['SOMFY_POD']
    
except KeyError:
    print("Environment variables not set!")

if __name__ == "__main__":
    # Initialize the SomfyAPI object
    api = SomfyAPI(SOMFY_URL, SOMFY_EMAIL, SOMFY_PASSWORD, SOMFY_POD)

    # Login
    api.login()

    # Check token status
    status = api.check_token_status()

    # Print the status
    print(status)

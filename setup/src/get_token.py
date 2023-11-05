"""
This script retrieves a token from the SomfyAPI by logging in with the provided credentials and activating the generated token.
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

    # Generate a token
    token = api.generate_token()

    # Activate the token
    api.activate_token(token)
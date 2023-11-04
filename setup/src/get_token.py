"""
This script retrieves a token from the SomphyAPI by logging in with the provided credentials and activating the generated token.
"""
import os
from somphy_api import SomphyAPI

try:
    SOMPHY_URL = os.environ['SOMPHY_URL']
    SOMPHY_EMAIL = os.environ['SOMPHY_EMAIL']
    SOMPHY_PASSWORD = os.environ['SOMPHY_PASSWORD']
    SOMPHY_POD = os.environ['SOMPHY_POD']

except KeyError:
    print("Environment variables not set!")
    
if __name__ == "__main__":
    # Initialize the SomphyAPI object
    api = SomphyAPI(SOMPHY_URL, SOMPHY_EMAIL, SOMPHY_PASSWORD, SOMPHY_POD)

    # Login
    api.login()

    # Generate a token
    token = api.generate_token()

    # Activate the token
    api.activate_token(token)
"""
This script retrieves a token from the SomphyAPI by logging in with the provided credentials and activating the generated token.
"""

import os
from somphy_api import SomphyAPI
from dotenv import load_dotenv

load_dotenv()

SOMPHY_URL = os.getenv('SOMPHY_URL')
SOMPHY_EMAIL = os.getenv('SOMPHY_EMAIL')
SOMPHY_PASSWORD = os.getenv('SOMPHY_PASSWORD')
SOMPHY_POD = os.getenv('SOMPHY_POD')

if __name__ == "__main__":
    # Initialize the SomphyAPI object
    api = SomphyAPI(SOMPHY_URL, SOMPHY_EMAIL, SOMPHY_PASSWORD, SOMPHY_POD)

    # Login
    api.login()

    # Generate a token
    token = api.generate_token()

    # Activate the token
    api.activate_token(token)
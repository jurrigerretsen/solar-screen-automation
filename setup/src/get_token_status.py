"""
This script loads environment variables and uses them to initialize a SomphyAPI object. 
It then logs in and checks the token status. Finally, it prints the status.
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

    # Check token status
    status = api.check_token_status()

    # Print the status
    print(status)

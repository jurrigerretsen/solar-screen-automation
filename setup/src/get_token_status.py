"""
This script loads environment variables and uses them to initialize a SomphyAPI object. 
It then logs in and checks the token status. Finally, it prints the status.
"""
import os
import os
from dotenv import load_dotenv
from somphy_api import SomphyAPI

# Load environment variables
load_dotenv()

# Get environment variables
SOMPHY_URL = os.getenv("SOMPHY_URL")
SOMPHY_EMAIL = os.getenv("SOMPHY_EMAIL")
SOMPHY_PASSWORD = os.getenv("SOMPHY_PASSWORD")
SOMPHY_POD = os.getenv("SOMPHY_POD")

if __name__ == "__main__":
    # Initialize the SomphyAPI object
    api = SomphyAPI(SOMPHY_URL, SOMPHY_EMAIL, SOMPHY_PASSWORD, SOMPHY_POD)

    # Login
    api.login()

    # Check token status
    status = api.check_token_status()

    # Print the status
    print(status)

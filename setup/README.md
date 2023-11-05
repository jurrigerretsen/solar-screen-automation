# Somphy API Python Scripts
This repository contains three Python scripts that interact with the Somphy API:
- `somphy_api.py`: This script contains the `SomphyAPI` class, which is used to interact with the Somphy API. It includes methods for logging in to Somphy and retrieving token status.

- `get_token_status.py`: This script uses the `SomphyAPI` class to retrieve and print the status of a Somphy token.

- `get_token.py`: This script uses the `SomphyAPI` class to retrieve and print a Somphy token. This script will create tokens in Somphy, so it's best not to call it too frequently.

## Usage
This project uses Poetry for dependency management and virtual environments, and .env for environment variables.

First, install the required dependencies:
```
poetry install
```

To use these scripts, you need to provide your Somphy credentials. These can be provided in a .env file:
```
SOMPHY_URL=<your-somphy-url>
SOMPHY_EMAIL=<your-somphy-email>
SOMPHY_PASSWORD=<your-somphy-password>
SOMPHY_POD=<your-somphy-pod>
```

Then, you can run the scripts like this:
```
poetry run -vvv python src/get_token.py
poetry run -vvv python src/get_token_status.py
```

## Testing
To run the unit tests, use the following command:
```
poetry run python -m unittest test_get_token_status.py
```

## License
This project is licensed under the MIT License.
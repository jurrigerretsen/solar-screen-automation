# Overkiz API Project

This project contains a Python script to interact with the Overkiz API.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
    - `overkiz.py`: contains the `OverkizAPI` class for interacting with the Overkiz API.
- `tests`: the folder to maintain tests
    - `test_overkiz.py`: contains the unit tests for the `OverkizAPI` class.

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (on Windows, use `env\Scripts\activate`)
5. Install the required dependencies: `pip install -r requirements.txt`
6. Create a `.env` file in the root of the project and add your Overkiz credentials:

    ```properties
    SOMPHY_URL=your_overkiz_url
    SOMPHY_EMAIL=your_email@example.com
    SOMPHY_PASSWORD=your_password
    SOMPHY_POD=your_pod_pin
    ```

7. Run the script: `python src/overkiz.py`

## Running Tests

To run the tests, use the following command: `python -m unittest -k TestOverkizAPI`
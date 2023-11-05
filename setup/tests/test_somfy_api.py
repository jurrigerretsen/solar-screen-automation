import unittest
from unittest.mock import patch, MagicMock
from src.somfy_api import SomfyAPI


class TestSomfyAPI(unittest.TestCase):
    @patch("requests.post")
    def test_login(self, mock_post):
        """
        Test the login method of the SomfyAPI class.

        This method tests that the login method of the SomfyAPI class sends the correct
        request to the Somfy API and returns the correct session ID.

        Args:
            mock_post (MagicMock): A mock of the requests.post method.

        Returns:
            None
        """
        # Mock the response from requests.post
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.cookies.get.return_value = "mock_session_id"
        mock_post.return_value = mock_response

        # Initialize the SomfyAPI object
        api = SomfyAPI("mock_url", "mock_email", "mock_password", "mock_pod")

        # Assert that requests.post was called with the correct arguments
        mock_post.assert_called_once_with(
            "https://mock_url/enduser-mobile-web/enduserAPI/login",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"userId": "mock_email", "userPassword": "mock_password"},
        )

        # Assert that the login method returns the correct session ID
        self.assertEqual(api.jsessionid, "mock_session_id")

    @patch("requests.get")
    def test_get_token_status(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "label": "Mock token",
                "gatewayId": "1234-5678-9012",
                "gatewayCreationTime": 1234567890000,
                "uuid": "abcd1234-a123-456a-a12b-a123b4c56d78",
                "scope": "mockmode",
            },
            {
                "label": "Mock token 2",
                "gatewayId": "9012-3456-7890",
                "gatewayCreationTime": 2345678901000,
                "uuid": "efgh5678-b234-789b-b23c-b234d5e67f89",
                "scope": "mockmode2",
            },
        ]
        mock_get.return_value = mock_response

        # Initialize the SomfyAPI object
        api = SomfyAPI("mock_url", "mock_email", "mock_password", "mock_pod")

        # Call the get_token_status method
        token_status = api.get_token_status()

        # Assert that requests.get was called with the correct arguments
        mock_get.assert_called_once_with(
            "https://mock_url/enduser-mobile-web/enduserAPI/setup/gateway/1234-5678-9012/token",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer mock_token",
            },
        )

        # Assert that the get_token_status method returns the correct data
        self.assertEqual(token_status, mock_response.json.return_value)


if __name__ == "__main__":
    unittest.main()

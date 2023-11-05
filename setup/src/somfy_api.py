import requests
import os

class SomfyAPI:
    """
    A class used to interact with the Somfy API.

    Attributes
    ----------
    url : str
        The URL of the Somfy API.
    email : str
        The email address of the user.
    password : str
        The password of the user.
    pod : str
        The pod of the user.
    jsessionid : str
        The session ID of the user.

    Methods
    -------
    login()
        Logs in the user and returns the session ID.
    generate_token()
        Generates a token for the user.
    activate_token(token, label="Local token", scope="devmode")
        Activates a token for the user.
    check_token_status()
        Checks the status of the user's token.
    """

    def __init__(self, url, email, password, pod):
        self.url = url
        self.email = email
        self.password = password
        self.pod = pod
        self.jsessionid = self.login()

    def login(self):
        """
        Logs in the user and returns the session ID.

        Returns
        -------
        str
            The session ID of the user.
        """
        endpoint = f"https://{self.url}/enduser-mobile-web/enduserAPI/login"
        headers = {"Content-Type": "application/json"}
        body = {"userId": self.email, "userPassword": self.password}
        response = requests.post(endpoint, headers=headers, data=body)
        if response.status_code == 200:
            return response.cookies.get("JSESSIONID")
        else:
            response.raise_for_status()

    def generate_token(self):
        """
        Generates a token for the user.

        Returns
        -------
        str
            The generated token.
        """
        endpoint = f"https://{self.url}/enduser-mobile-web/enduserAPI/config/{self.pod}/local/tokens/generate"
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"JSESSIONID={self.jsessionid}",
        }
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()["token"]
        else:
            response.raise_for_status()

    def activate_token(self, token, label="Local token", scope="devmode"): # todo: input token & scope as parameters
        """
        Activates a token for the user.

        Parameters
        ----------
        token : str
            The token to activate.
        label : str, optional
            The label for the token, by default "Toto token".
        scope : str, optional
            The scope for the token, by default "devmode".
        """
        endpoint = f"https://{self.url}/enduser-mobile-web/enduserAPI/config/{self.pod}/local/tokens"
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"JSESSIONID={self.jsessionid}",
        }
        body = {"label": label, "token": token, "scope": scope}
        response = requests.post(endpoint, headers=headers, json=body)
        if response.status_code != 200:
            response.raise_for_status()

    def check_token_status(self):
        """
        Checks the status of the user's token.

        Returns
        -------
        dict
            The status of the user's token.
        """
        endpoint = f"https://{self.url}/enduser-mobile-web/enduserAPI/config/{self.pod}/local/tokens/devmode"
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"JSESSIONID={self.jsessionid}",
        }
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

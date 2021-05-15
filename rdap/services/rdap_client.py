import json
import requests
from .retry_strategy import SimpleRetryStrategy

class RdapClient:
    """
    In charge of gathering the respective domain data.
    """

    DELAY = 500 # ms
    RETRY_COUNT = 3
    
    def __init__(self) -> None:
        self._client = requests.Session()
        self._retry_strategy = None
        self._retry_policy = None
        self._headers = {
            "Accept" : "application/json",
            "content-type" : "application/json",
        }
    
    def _get(self, url) -> None:
        response = self._client.get(
            url=url,
            headers=self._headers
        )

        if response.status_code == 200:
            return response.json()
    
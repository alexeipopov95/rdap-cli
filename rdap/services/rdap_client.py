import requests

class RdapClient:
    
    def __init__(self) -> None:
        self._client = requests.Session()
        self._headers = {
            "Accept" : "application/json",
            "content-type" : "application/json",
        }
    
    def get(self, link:str) -> dict:
        response = self._client.get(
            url=link,
            headers=self._headers
        )
        
        # TODO I have to implement a retry policy and strategy.
        if response.status_code == 404:
            context = {
                "status" : True,
                "content" : {},
            }
        else:
            context = {
                "status" : False,
                "content" : response.json(),
            }

        return context

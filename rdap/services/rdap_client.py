import requests


class RdapClient:
    """
    In charge of gathering the respective domain data.
    """
    
    def __init__(self) -> None:
        self.client = requests.Session()
        self.retry_policy = None
    
    @classmethod
    def get(cls) -> None:
        pass

    @classmethod
    def post(cls) -> None:
        pass

    
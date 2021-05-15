import os
from datetime import datetime
#from rdap.utils.endpoints import RDAP_DNS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RDAP_DNS_FILENAME = "dns.json"

class RdapApi:
    #RDAP_DNS = RDAP_DNS

    def __init__(self, domain) -> None:
        self.domain = domain
        self.file_path = os.path.join(BASE_DIR, "templates", "dns")

        if not os.listdir(self.file_path):
            # TODO: RdapClient must retrive the DNS file and parse it.
            pass

        else:
            file_date = os.path.getmtime(RDAP_DNS_FILENAME)
            file_date = datetime.fromtimestamp(file_date)
            now = datetime.now()

            if (now - file_date).days > 7:
                # TODO: RdapClient update the DNS file.
                pass

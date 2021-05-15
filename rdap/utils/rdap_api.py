import os
from datetime import datetime
from rdap.utils.endpoints import RDAP_DNS
from rdap.utils.utils import (
    _load_file_data,
    _save_file_data,
    _string_to_datetime,
)
from rdap.common.constants import RdapDomainEvents

PERIODS = [
    RdapDomainEvents.REGISTRATION,
    RdapDomainEvents.EXPIRATION,
    RdapDomainEvents.LAST_CHANGED,
    RdapDomainEvents.LAST_CHANGED_RDAP
]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RDAP_DNS_FILENAME = "dns.json"

class RdapApi:
    RDAP_DNS = RDAP_DNS

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

    @classmethod
    def _find_url(cls, services:list, domain:str) -> str:
        """parse the list of services and tlds to return a
        valid url to query the dns entity.

        Args:
            services (list): [list of tlds and services]
            domain (str, optional): [domain name]. Defaults to "google.com".

        Returns:
            str: [return an url]
        """

        for tld, service in services:
            if domain.endswith(tuple(tld)):
                return "{0}domain/{1}".format(
                    service[0], domain
                )
        return

    @classmethod
    def get_contex_data(cls, domain:str) -> dict:
        """
        return a valid endpoint to query into the dns sites
        Args:
            domain (str): [it requires the domain name]
        Returns:
            str: [return a valid endpoint if the tld is part of RDAP]
        """
        data = _load_file_data(RDAP_DNS_FILENAME)
        context = {
            "description" : data['description'],
            "publication" : data['publication'],
            "url" : cls._find_url(data['services'], domain),
        }
        return context

    @classmethod
    def get_nameservers(cls, context_data:dict) -> list:
        """return a list of nameservers related to the domain
        Args:
            context_data (dict): [description]
        Returns:
            list: [a list of nameservers]
        """

        dns_list = []

        if 'nameservers' in context_data['response']['data']:
            while len(dns_list) < (len(context_data['response']['data']['nameservers'])):
                dns_list.append(context_data['response']['data']['nameservers'][len(dns_list)]['ldhName'].lower())

        return dns_list

    @classmethod
    def get_events(cls, context_data:dict) -> dict:

        events = {}

        for event in context_data['response']['data']['events']:

            if event['eventAction'] == RdapDomainEvents.REGISTRATION:
                events['create_date'] = _string_to_datetime(event['eventDate'])

            elif event['eventAction'] == RdapDomainEvents.EXPIRATION:
                events['expire_date'] = _string_to_datetime(event['eventDate'])

            elif event['eventAction'] == RdapDomainEvents.LAST_CHANGED:
                events['update_date'] = _string_to_datetime(event['eventDate'])

            elif event['eventAction'] == RdapDomainEvents.LAST_CHANGED_RDAP:
                events['update_date_rdap'] = _string_to_datetime(event['eventDate'])


        return events



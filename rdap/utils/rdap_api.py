import os
import click
from datetime import datetime

from rdap.utils.endpoints import RDAP_DNS
from rdap.utils.utils import (
    datetime_to_string,
    formater,
    load_file_data,
    save_file_data,
    string_to_datetime,
)
from rdap.common.constants import (
    RdapDomainEvents,
    FormatterStatus,
    TextFormatConstants,
)
from rdap.services.rdap_client import RdapClient

PERIODS = [
    RdapDomainEvents.REGISTRATION,
    RdapDomainEvents.EXPIRATION,
    RdapDomainEvents.LAST_CHANGED,
    RdapDomainEvents.LAST_CHANGED_RDAP
]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RDAP_DNS_FILENAME = "dns.json"
CACHE_FILE_NAME = "cache.json"
UNDEFINED_DATA = "Undefined"


def save_history(method): # esta es la funcion principal
    def inner(cls):
        CACHE_FILE_DIR = os.path.join(BASE_DIR, "templates", "history")
        CACHE_FILE_PATH = os.path.join(BASE_DIR, "templates", "history", CACHE_FILE_NAME)

        if not os.listdir(CACHE_FILE_DIR):
            save_file_data(
                [],
                CACHE_FILE_PATH,
                TextFormatConstants.JSON
            )

        output = load_file_data(CACHE_FILE_PATH)
        output.append(method(cls))
        save_file_data(output, CACHE_FILE_PATH, TextFormatConstants.JSON)


        return method(cls)
    return inner

class RdapApi:
    CLIENT = RdapClient()
    FILE_DIR = os.path.join(BASE_DIR, "templates", "dns")
    FILE_PATH = os.path.join(BASE_DIR, "templates", "dns", RDAP_DNS_FILENAME)


    def __init__(self, domain:str) -> None:
        self.domain = domain

        # TODO: Manage to resolve if the file does not download properly
        if not os.listdir(self.FILE_DIR):
            click.echo(
                formater(
                    message="Preparing dns data. This step happen only once.",
                    status=FormatterStatus.INFO
                )
            )
            response = self.CLIENT._get(RDAP_DNS)
            save_file_data(response, self.FILE_PATH, _type=TextFormatConstants.JSON)
            click.echo(
                formater(
                    message="DONE",
                    status=FormatterStatus.INFO
                )
            )

        else:
            file_date = os.path.getmtime(self.FILE_PATH)
            file_date = datetime.fromtimestamp(file_date)

            if (datetime.now() - file_date).days > 7:
                response = self.CLIENT._get(RDAP_DNS)
                save_file_data(response, RDAP_DNS_FILENAME, _type=TextFormatConstants.JSON)

    @classmethod
    def _get_context_data(cls, domain:str) -> dict:
        """
        return a valid endpoint to query into the dns sites
        Args:
            domain (str): [it requires the domain name]
        Returns:
            str: [return a valid endpoint if the tld is part of RDAP]
        """

        data = load_file_data(cls.FILE_PATH)
        context = {
            "description" : data['description'],
            "publication" : data['publication'],
            "url" : cls._find_url(data['services'], domain),
        }
        return context

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
    def _get_nameservers(cls, context_data:dict) -> list:
        """return a list of nameservers related to the domain
        Args:
            context_data (dict): [description]
        Returns:
            list: [a list of nameservers]
        """

        dns_list = []

        if 'nameservers' in context_data:
            while len(dns_list) < (len(context_data['nameservers'])):
                dns_list.append(context_data['nameservers'][len(dns_list)]['ldhName'].lower())

        return dns_list

    @classmethod
    def _get_events(cls, context_data:dict) -> dict:

        events = {}

        for event in context_data['events']:

            if event['eventAction'] == RdapDomainEvents.REGISTRATION:
                events['create_date'] = string_to_datetime(event['eventDate'])

            elif event['eventAction'] == RdapDomainEvents.EXPIRATION:
                events['expire_date'] = string_to_datetime(event['eventDate'])

            elif event['eventAction'] == RdapDomainEvents.LAST_CHANGED:
                events['update_date'] = string_to_datetime(event['eventDate'])

            elif event['eventAction'] == RdapDomainEvents.LAST_CHANGED_RDAP:
                events['update_date_rdap'] = string_to_datetime(event['eventDate'])


        return events

    @classmethod
    def _get_owner_data(cls, contex_data:dict, domain:str) -> dict:

        data = {}
        if domain.endswith(".ar"):
            data['entity'] = "Nic Argentina"
            data['id'] = contex_data['entities'][0]['handle']

            url = contex_data['entities'][0]['links'][0]['href']
            name = cls.CLIENT._get(url)
            data['name'] = name['vcardArray'][1][1][-1]                

        else:
            data['entity'] = contex_data['entities'][0]['vcardArray'][1][1][-1]
        
        return data

    @save_history
    def get_domain_data(self) -> dict:

        context_data = self._get_context_data(domain=self.domain)
        domain_data = self.CLIENT._get(
            url= context_data.get("url", None)
        )

        if not self.CLIENT.VALID_URL:
            click.echo(
                formater(
                    message=(
                        "That TLD looks like it is not part of RDAP protocol yet. "
                        "Cannot gather any information about it."
                    ),
                    status=FormatterStatus.ERROR
                )
            )

        elif not domain_data:
            click.echo(
                formater(
                    message=(
                        f"{self.domain} is available to register. "
                        f"For more information you can got here: {context_data.get('url')}"
                    ),
                    status=FormatterStatus.INFO
                )
            )

        else:
            events = self._get_events(domain_data)
            owner_data = self._get_owner_data(domain_data, self.domain)

            data = {
                "domain" : self.domain,
                "dns" : self._get_nameservers(domain_data) or UNDEFINED_DATA,
                "create_at" : datetime_to_string(events.get("create_date")) or UNDEFINED_DATA,
                "expire_at" : datetime_to_string(events.get("expire_date")) or UNDEFINED_DATA,
                "update_at" : datetime_to_string(events.get("update_date")) or UNDEFINED_DATA,
                "update_at_rdap" : datetime_to_string(events.get("update_date_rdap")) or UNDEFINED_DATA,
                "entity" : owner_data.get("entity", UNDEFINED_DATA),
                "id" : owner_data.get("id", UNDEFINED_DATA),
                "name" : owner_data.get("name", UNDEFINED_DATA)
            }

            return data

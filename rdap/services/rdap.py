import os
import uuid
from datetime import datetime
from rdap.common.endpoints import RDAP_DNS
from rdap.services.rdap_client import RdapClient
from rdap.common.utils import (
    load_file_data,
    save_file_data,
    string_to_datetime,
    datetime_to_string,
    form_hostname,
)
from rdap.common.constants import (
    RdapDomainEvents,
    TextFormatConstants,
)
from rdap.settings import (
    BASE_DIR,
    RDAP_DNS_FILENAME,
    UNDEFINED_DATA,
    CACHE_FILE_PATH,
    CACHE_LIMIT_RECORDS,
)


def save_history(method):
    """
    Decorator designed to save the query into a json-file when 'gather' command
    or 'check' were called.

    Args:
        method ([type]): Receive classmethod.
    """

    def save(cls):
        data = method(cls)

        if not os.path.isfile(CACHE_FILE_PATH):
            save_file_data([], CACHE_FILE_PATH, TextFormatConstants.JSON)

        data["id"] = str(uuid.uuid4())[:8]
        data["timestamp"] = datetime_to_string(datetime.now())
        output = load_file_data(CACHE_FILE_PATH)

        if len(output) >= CACHE_LIMIT_RECORDS:
            output.pop(0)

        output.append(data)

        save_file_data(output, CACHE_FILE_PATH, TextFormatConstants.JSON)
        return method(cls)

    return save


class RdapApi:
    CLIENT = RdapClient()
    DNS_FILE_DIR = os.path.join(BASE_DIR)
    DNS_FILE_PATH = os.path.join(BASE_DIR, RDAP_DNS_FILENAME)
    IS_PART_OF_RDAP_PROTOCOL = False
    AVAILABLE_TO_REGISTER = False
    DOMAIN_HOST = None

    def __init__(self, domain: str) -> None:
        self.domain = domain

        if not os.path.isfile(self.DNS_FILE_PATH):
            response = self.CLIENT.get(RDAP_DNS).get("content")
            save_file_data(response, self.DNS_FILE_PATH, TextFormatConstants.JSON)

        else:
            file_date = os.path.getmtime(self.DNS_FILE_PATH)
            file_date = datetime.fromtimestamp(file_date)

            if (datetime.now() - file_date).days > 7:
                response = self.CLIENT.get(RDAP_DNS).get("content")
                save_file_data(response, RDAP_DNS_FILENAME, TextFormatConstants.JSON)

        self.DOMAIN_HOST = self._get_host(self.domain)

    @classmethod
    def _get_host(cls, domain: str) -> None:
        """
        In charge of getting the domain host and determine
        if the domain is part of the RDAP protocol or not.

        Args:
            domain (str): [Domain name. I.e: 'example.com']

        """

        context = load_file_data(cls.DNS_FILE_PATH)

        for tld, service in context.get("services"):
            if domain.endswith(tuple(tld)):
                cls.IS_PART_OF_RDAP_PROTOCOL = True
                cls.DOMAIN_HOST = "{0}domain/{1}".format(service[0], domain)

    @classmethod
    def _get_scheme(cls, domain: str) -> dict:
        """
        Returns the scheme that will later be rendered in the commands.

        Args:
            domain (str): [Domain name. I.e: 'example.com']
        Returns:
            dict: [A full scheme of the info to be showed on screen later]
        """

        schema = {
            "is_rdap": cls.IS_PART_OF_RDAP_PROTOCOL,
            "status": False,
            "domain": domain,
            "host": form_hostname(cls.DOMAIN_HOST),
            "query_host": cls.DOMAIN_HOST or UNDEFINED_DATA,
            "content": {
                "domain": domain,
                "dns": UNDEFINED_DATA,
                "create_at": UNDEFINED_DATA,
                "expire_at": UNDEFINED_DATA,
                "update_at": UNDEFINED_DATA,
                "update_at_rdap": UNDEFINED_DATA,
                "entity": UNDEFINED_DATA,
                "registrant_id": UNDEFINED_DATA,
                "name": UNDEFINED_DATA,
            },
        }

        return schema

    @classmethod
    def _get_nameservers(cls, context_data: dict) -> list:
        """
        Return a list of nameservers related to the domain.

        Args:
            context_data (dict): [
                The complete payload comming from the host
            ]
        Returns:
            list: [a list of nameservers]
        """

        dns_list = []
        if "nameservers" in context_data:
            while len(dns_list) < (len(context_data["nameservers"])):
                dns_list.append(
                    context_data["nameservers"][len(dns_list)]["ldhName"].lower()
                )

        return dns_list

    @classmethod
    def _get_events(cls, context_data: dict) -> dict:
        """
        In charge of parsing the context data and look up for the
        domain events (expiration date, creation date, etc.)

        Args:
            context_data (dict): [
                The complete payload comming from the host
            ]
        Returns:
            dict: [A dictionary with the timestamps of the domain]
        """

        events = {}
        if context_data:
            for event in context_data["events"]:

                if event["eventAction"] == RdapDomainEvents.REGISTRATION:
                    events["create_at"] = datetime_to_string(
                        string_to_datetime(event["eventDate"])
                    )

                elif event["eventAction"] == RdapDomainEvents.EXPIRATION:
                    events["expire_at"] = datetime_to_string(
                        string_to_datetime(event["eventDate"])
                    )

                elif event["eventAction"] == RdapDomainEvents.LAST_CHANGED:
                    events["update_at"] = datetime_to_string(
                        string_to_datetime(event["eventDate"])
                    )

                elif event["eventAction"] == RdapDomainEvents.LAST_CHANGED_RDAP:
                    events["update_at_rdap"] = datetime_to_string(
                        string_to_datetime(event["eventDate"])
                    )

        return events

    @classmethod
    def _get_owner_data(cls, contex_data: dict, domain: str) -> dict:
        """
        In charge of parsing the context data and look up for the
        domain specific data, making focus on the owners data.

        Args:
            context_data (dict): [
                The complete payload comming from the host
            ]
            domain (str): [Domain name. I.e: 'example.com']

        Returns:
            dict: [Returns a dictionary with the domain owner data]
        """

        data = {}
        if contex_data:
            if domain.endswith(".ar"):
                data["entity"] = "Nic Argentina"
                data["id"] = contex_data["entities"][0]["handle"]

                url = contex_data["entities"][0]["links"][0]["href"]
                name = cls.CLIENT.get(url).get("content")
                data["name"] = name["vcardArray"][1][1][-1]

            else:
                data["entity"] = contex_data["entities"][0]["vcardArray"][1][1][-1]

        return data

    @classmethod
    def _get_context_data(cls) -> dict:
        """
        Make a request into the domain host and retrive all the
        context data required to be parsed latter.

        Returns:
            dict: [Return the full context data from the host]
        """

        return cls.CLIENT.get(cls.DOMAIN_HOST)

    @save_history
    def query(self) -> dict:
        """
        In charge of gathering all the information about the domain
        and putting together a context to be delivered later.

        Returns:
            dict: [Return the formated sheme with the domain information]
        """
        schema = self._get_scheme(self.domain)

        if not self.IS_PART_OF_RDAP_PROTOCOL:
            return schema

        context = self._get_context_data()
        if context.get("status"):
            schema["status"] = True
            return schema

        dates = self._get_events(context.get("content"))
        owner_data = self._get_owner_data(context.get("content"), self.domain)

        schema["content"]["dns"] = ", ".join(
            self._get_nameservers(context.get("content"))
        )
        schema["content"]["create_at"] = dates.get("create_at" or UNDEFINED_DATA)
        schema["content"]["expire_at"] = dates.get("expire_at" or UNDEFINED_DATA)
        schema["content"]["update_at"] = dates.get("update_at" or UNDEFINED_DATA)
        schema["content"]["update_at_rdap"] = dates.get(
            "update_at_rdap" or UNDEFINED_DATA
        )
        schema["content"]["entity"] = owner_data.get("entity" or UNDEFINED_DATA)
        schema["content"]["registrant_id"] = owner_data.get("id" or UNDEFINED_DATA)
        schema["content"]["name"] = owner_data.get("name" or UNDEFINED_DATA)

        return schema

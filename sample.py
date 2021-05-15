import os
import json
from datetime import datetime
import dateutil.parser
import requests

"""
response = requests.get(url="https://data.iana.org/rdap/dns.json")
with open(RDAP_DNS_FILENAME, "w") as op:
    op.write(response.text)
"""

def _load_file_data(filename:str) -> dict:
    """receive a file name and return as a dict
    Args:
        filename (str): [filename]
    Returns:
        dict: [return a dict object]
    """

    with open(filename, "r") as output:
        data = json.load(output)
    return data



def _get_dns_file_description(data:dict) -> str:
    return data['description']

def _get_dns_file_publication(data:dict) -> datetime:
    return _string_to_datetime(data['publication'])

def _get_dns_file_services(data:dict) -> list:
    return data['services']

def _parse_endpoint(services:list, domain:str="google.com") -> str:
    """parse the list of services and tld and return 
    the respective url to make the request

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


def base():
    data = _load_file_data("dns.json") # works
    #description = _get_dns_file_description(data)
    #publication = _get_dns_file_publication(data)
    services = _get_dns_file_services(data)
    endpoint = _parse_endpoint(services)
    print(endpoint)


    

print(base())






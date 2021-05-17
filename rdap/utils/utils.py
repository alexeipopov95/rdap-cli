import click
import json
import dateutil.parser
import validators
from datetime import datetime

from rdap.commands.exceptions import (
    GatherEmptyParam,
    GatherInvalidDomainName
)
from rdap.common.constants import (
    FormatterStatus,
)


def formater(message:str, status:str) -> click.style:
    status_color = FormatterStatus.formater_color_map.get(status, "INFO")
    return click.style(
        f"[{status}] - {message}",
        fg=status_color
    )

def load_file_data(filename:str) -> dict:
    """receive a file name and return as a dict
    Args:
        filename (str): [filename]
    Returns:
        dict: [return a dict object]
    """

    with open(filename, "r") as output:
        data = json.load(output)
    return data

def save_file_data(data:dict, filename:str, _type:str="json") -> None:
    """Save data in a file

    Args:
        data (dict): [data to be saved]
        filename (str): [filename where data is going to be saved]
        _type (str): [Specify the file type]
    """

    with open(filename, "w") as input:

        if not _type == "json":
            input.write(data)
        else:
            json.dump(data, input)

def string_to_datetime(date:str) -> datetime:
    if date:
        return dateutil.parser.parse(date).replace(tzinfo=None)
    return date

def datetime_to_string(date:datetime) -> str:
    if date:
        return date.strftime("%Y-%m-%d %H:%M:%S")
    return date

def domain_validator(domain:str) -> bool:
    """Based on a regex define if a domain is valid or not
    Args:
        domain (str): [Domain name]
    Returns:
        bool: [True or False]
    """

    if validators.domain(domain):
        return True

def domain_checker(domain:str) -> None:
    """[summary]
    Args:
        domain (str): [description]
    """

    if not domain or domain.strip() == "":
        raise GatherEmptyParam(
            f"Domain was None, please provide a valid domain using --domain option"
        )

    if not domain_validator(domain):
        raise GatherInvalidDomainName(
            f"Domain '{domain}' is not a valid domain name."
        )

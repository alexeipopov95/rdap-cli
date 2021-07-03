import os
import click
import json
import dateutil.parser
import tldextract
from datetime import datetime
from rdap.settings import UNDEFINED_DATA
from rdap.common.exceptions import (
    NotSupportedFileFormat,
)
from rdap.common.constants import (
    TextFormatConstants,
    MessageColors,
    DomainAvailability,
)

AVAILABLE_EXTENCION = (
    TextFormatConstants.JSON,
    TextFormatConstants.TEXT,
)


def load_file_data(filename: str) -> dict or str:
    """Receive a filename, try to check if the format is valid and
    return the respective data according to its format.

    Args:
        filename (str): [Filename. I.e: my_file.json]
    Raises:
        FileNotFoundError: [raise if the file is not found]
    Returns:
        dict or str: [
            deppending on the file format return
            a dict object or a str
        ]
    """

    if not os.path.isfile(filename):
        raise FileNotFoundError

    with open(filename, "r") as output:
        if filename.endswith(TextFormatConstants.JSON):
            data = json.load(output)
        elif filename.endswith(TextFormatConstants.TEXT):
            data = output.read()

    return data


def save_file_data(data: dict, filename: str, _type: str) -> None:
    """Save the data in the corresponding file.

    Args:
        data (dict): [Data to be saved]
        filename (str): [Filename. I.e: my_file.json]
        _type (str): [Define the file type]

    Raises:
        NotSupportedFileFormat: [
            This exception occurs when the user entersa text
            format that is not valid or is not supported by the cli.
        ]
    """

    if _type not in AVAILABLE_EXTENCION:
        raise NotSupportedFileFormat(f"The extension '.{_type}' is not supported yet")

    with open(filename, "w") as input:

        if _type == TextFormatConstants.JSON:
            json.dump(data, input)

        elif _type == TextFormatConstants.TEXT:
            data = convert_dict_into_txt(data)
            input.write(data)


def string_to_datetime(date: str) -> datetime:
    """Convert a datetime stringified into a datetime object

    Args:
        date (str): [Datetime as string]

    Returns:
        datetime: [Datetime as datetime.datetime]
    """

    if date:
        return dateutil.parser.parse(date).replace(tzinfo=None)
    return date


def datetime_to_string(date: datetime) -> str:
    """Convert a datetime object into a datetime stringified.

    Args:
        date (datetime): [Datetime object]

    Returns:
        str: [Datetime as String]
    """

    if date:
        return date.strftime("%Y-%m-%d %H:%M")
    return date


def get_subdomain(domain: str) -> str:
    """Receive a domain and parse it returning the subdomain
    based on a regex pattern. (external library)

    Args:
        domain (str): [Receive a domain. I.e example.com]

    Returns:
        str: [
            Return only the subdomain of the domain.
            I.e if blog.example.com -> blog
        ]
    """
    try:
        return tldextract.extract(domain).subdomain
    except TypeError:
        return ""


def get_domain(domain: str) -> str:
    """Receive a domain and parse it returning the domain
    based on a regex pattern. (external library)

    Args:
        domain (str): [Receive a domain. I.e example.com]

    Returns:
        str: [
            Return only the subdomain of the domain.
            I.e if blog.example.com -> example
        ]
    """
    try:
        return tldextract.extract(domain).domain
    except TypeError:
        return ""


def get_suffix(domain: str) -> str:
    """Receive a domain and parse it returning the suffix
    based on a regex pattern. (external library)

    Args:
        domain (str): [Receive a domain. I.e example.com]

    Returns:
        str: [
            Return only the suffix of the domain.
            I.e if blog.example.com -> com
        ]
    """
    try:
        return tldextract.extract(domain).suffix
    except TypeError:
        return ""


def form_hostname(data: str) -> str:
    """In charge of forming a hostname based on the data
    received. If data is true return a descent hostname.
    I.e https://example.com

    Args:
        data (str): [receive a domain name or host name]

    Returns:
        str: [a more beautiful hostname]
    """
    domain = get_domain(data)
    suffix = get_suffix(data)

    if domain != "" and suffix != "":
        return "https://{0}.{1}/".format(domain, suffix)
    return UNDEFINED_DATA


def get_availability(data: dict) -> str:
    """This is to avoid repeating the code so many times.
    It is mainly used to define the domain availability status and color it.

    Args:
        data (dict): [dict with some data from the context]

    Returns:
        str: [return a stringified version of the domain's availability]
    """

    if data.get("status"):
        availability = click.style(
            DomainAvailability.AVAILABLE,
            fg=DomainAvailability.availability_color_map.get(
                DomainAvailability.AVAILABLE
            ),
            bold=True,
        )
    else:
        availability = click.style(
            DomainAvailability.UNAVAILABLE,
            fg=DomainAvailability.availability_color_map.get(
                DomainAvailability.UNAVAILABLE
            ),
            bold=True,
        )

    return availability


def format_domain_output(data: dict) -> str:
    """This is to avoid repeating the code so many times.
    It is mainly used to format a user-friendly view when
    it is called from the gather or the check commands.

    Args:
        data (dict): [dict with data from the context]

    Returns:
        str: [return a stringified version of the domain's data]
    """

    is_available = get_availability(data)
    data = data["content"]
    dns = " \n\t\t    ".join(data.get("dns").split(","))
    message = f"""
        Domain: {
            click.style(data.get("domain").upper(), fg=MessageColors.WHITE, bold=True)
        }
        Status: {is_available}

        Nameservers: {
            click.style(dns, fg=MessageColors.WHITE, bold=True)
        }

        Create date: {
            click.style(
                data.get(
                    "create_at", UNDEFINED_DATA
                ), fg=MessageColors.WHITE, bold=True
            )
        }
        Expire date: {
            click.style(
                data.get(
                    "expire_at", UNDEFINED_DATA
                ), fg=MessageColors.WHITE, bold=True
            )
        }
        Update date: {
            click.style(
                data.get(
                    "update_at", UNDEFINED_DATA
                ), fg=MessageColors.WHITE, bold=True
            )
        }
        Update date (RDAP): {
            click.style(
                data.get(
                    "updata_at_rdap", UNDEFINED_DATA
                ), fg=MessageColors.WHITE, bold=True
            )
        }

        Entity: {
            click.style(
                data.get(
                    "entity", UNDEFINED_DATA
                ), fg=MessageColors.WHITE, bold=True
            )
        }
        Name: {
            click.style(
                data.get(
                    "name", UNDEFINED_DATA
                ), fg=MessageColors.WHITE, bold=True
            )
        }
        Registrant ID: {
            click.style(
                data.get(
                    "registrant_id", UNDEFINED_DATA
                ), fg=MessageColors.WHITE, bold=True
            )
        }
    """
    return message


def convert_dict_into_txt(data: dict) -> str:
    """This function recursively converts the contents of a dictionary
    to plain text and then be delivered in a text file.

    Args:
        data (dict): [The data to be converted into txt]

    Returns:
        str: [The converted dictionary into text]
    """

    line = ""

    if isinstance(data, list):
        for elements in data:
            for key, value in elements.items():

                if isinstance(value, dict):
                    line += convert_dict_into_txt(value)
                else:
                    line += f"{key}: {value}\n"
    else:
        for key, value in data.items():

            if isinstance(value, dict):
                line += convert_dict_into_txt(value)
            else:
                line += f"{key}: {value}\n"

    return line

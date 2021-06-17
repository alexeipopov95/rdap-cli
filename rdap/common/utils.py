import os
import click
import json
import dateutil.parser
import tldextract
from datetime import datetime
from rdap.settings import UNDEFINED_DATA
from rdap.common.exceptions import (
    FileDoesNotExist,
    ImproperlyConfiguredFile,
    NotSupportedFormat,
)
from rdap.common.constants import (
    FormatterStatus,
    TextFormatConstants,
    MessageColors,
    DomainAvailability,
)

AVAILABLE_EXTENCION = (
    TextFormatConstants.JSON,
    TextFormatConstants.TEXT,
    #TextFormatConstants.YML,
)


def _json_file_parser(file) -> str:
    data = load_file_data(file)
    domain_list = data.get("domains")
    if not domain_list:
        raise ImproperlyConfiguredFile(
            f"The {TextFormatConstants.JSON} is expecting 'domains' as key field. "
            "Please make sure that the key is 'domains' and "
            "the value is a non empty array of domains."
        )

    return domain_list


def _txt_file_parser(file) -> str:
    data = load_file_data(file)
    return data.split("\n")


def _yml_file_parser() -> str:
    print("YML file parser")
    pass


FILE_PARSER_MAP = {
    TextFormatConstants.JSON : _json_file_parser,
    TextFormatConstants.TEXT : _txt_file_parser,
    #TextFormatConstants.YML : _yml_file_parser,
}


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

    if not os.path.isfile(filename):
        raise FileDoesNotExist(
            "The file you are trying to access does not exist yet."
        )


    with open(filename, "r") as output:
        if filename.endswith(TextFormatConstants.JSON):
            data = json.load(output)
        elif filename.endswith(TextFormatConstants.TEXT):
            data = output.read()
        elif filename.endswith(TextFormatConstants.YML):
            pass

    return data


def save_file_data(data:dict, filename:str, _type:str) -> None:
    """Save data in a file
    Args:
        data (dict): [data to be saved]
        filename (str): [filename where data is going to be saved]
        _type (str): [Specify the file type]
    """

    if _type not in AVAILABLE_EXTENCION:
        raise NotSupportedFormat(
            f"The extension '.{_type}' is not supported yet"
        )

    with open(filename, "w") as input:

        if _type == TextFormatConstants.JSON:
            json.dump(data, input)
        elif _type == TextFormatConstants.YML:
            pass 
        else:
            input.write(data)


def string_to_datetime(date:str) -> datetime:
    if date:
        return dateutil.parser.parse(date).replace(tzinfo=None)
    return date


def datetime_to_string(date:datetime) -> str:
    if date:
        return date.strftime("%Y-%m-%d %H:%M")
    return date


def file_parser(file:str):
    _, extension = file.split(".", 1)

    if not extension in AVAILABLE_EXTENCION:
        raise NotSupportedFormat(
            f"The extension '.{extension}' is not supported yet"
        )

    maped_file = FILE_PARSER_MAP.get(extension)
    return maped_file(file)


def get_subdomain(domain:str) -> str:
    try:
        return tldextract.extract(domain).subdomain
    except TypeError:
        return ''


def get_domain(domain:str) -> str:
    try:
        return tldextract.extract(domain).domain
    except TypeError:
        return ''


def get_suffix(domain:str) -> str:
    try:
        return tldextract.extract(domain).suffix
    except TypeError:
        return ''


def form_hostname(data:dict) -> str:
    domain = get_domain(data)
    suffix = get_suffix(data)

    if domain != '' and suffix != '':
        return "https://{0}.{1}/".format(domain, suffix)
    return UNDEFINED_DATA


def get_availability(data:dict) -> str:

    if data.get("status"):
        availability = click.style(
            DomainAvailability.AVAILABLE,
            fg=DomainAvailability.availability_color_map.get(
                DomainAvailability.AVAILABLE
            ),
            bold=True
        )
    else:
        availability = click.style(
            DomainAvailability.UNAVAILABLE,
            fg=DomainAvailability.availability_color_map.get(
                DomainAvailability.UNAVAILABLE
            ),
            bold=True
        )
    
    return availability


def format_domain_output(data:dict) -> str:

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
            click.style(data.get("create_at", UNDEFINED_DATA), fg=MessageColors.WHITE, bold=True)
        }
        Expire date: {
            click.style(data.get("expire_at", UNDEFINED_DATA), fg=MessageColors.WHITE, bold=True)
        }
        Update date: {
            click.style(data.get("update_at", UNDEFINED_DATA), fg=MessageColors.WHITE, bold=True)
        }
        Update date (RDAP): {
            click.style(data.get("updata_at_rdap", UNDEFINED_DATA), fg=MessageColors.WHITE, bold=True)
        }

        Entity: {
            click.style(data.get("entity", UNDEFINED_DATA), fg=MessageColors.WHITE, bold=True)
        }
        Name: {
            click.style(data.get("name", UNDEFINED_DATA), fg=MessageColors.WHITE, bold=True)
        }
        Registrant ID: {
            click.style(data.get("registrant_id", UNDEFINED_DATA), fg=MessageColors.WHITE, bold=True)
        }
    """
    return message

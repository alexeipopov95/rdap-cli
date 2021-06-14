import os
import click
import json
import dateutil.parser
import tldextract
from datetime import datetime

from rdap.common.exceptions import (
    EmptyFileError,
    ImproperlyConfiguredFile,
    NotSupportedFormat,
)
from rdap.common.constants import (
    FormatterStatus,
    TextFormatConstants,
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


def _is_empty_file(filename:str) -> None:
    if os.stat(filename).st_size == 0:
        raise EmptyFileError(
            f"{filename} is empty"
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

    _is_empty_file(filename)

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
        return date.strftime("%Y-%m-%d %H:%M:%S")
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

SAVE command
import os
from typing import Text
import click
from rdap.utils.rdap_api import RdapApi
from rdap.common.constants import FormatterStatus
from rdap.utils.utils import (
    domain_parser,
    formater,
    save_file_data
) 
from rdap.common.constants import TextFormatConstants


SAVE_RDAP_HELP_DOMAIN = (
    "You have to specify the domain name to be saved. "
)

SAVE_RDAP_HELP_FILE = (
    "You have to specify the file name where you want to save the info. "
    "It will save the file on your current working directory i.e: "
    "--file=result.txt or --file=result.json.\n\n "
    "-- Available formats are '.json' and '.txt'"
)

AVAILABLE_EXTENCION = (
    TextFormatConstants.JSON,
    TextFormatConstants.TEXT,
)


@click.command()
@click.option("-d", "--domain", required=True, help=SAVE_RDAP_HELP_DOMAIN)
@click.option("-f", "--file", required=True, help=SAVE_RDAP_HELP_FILE)
def save(domain:str, file:str) -> click.echo:
    """ Save the information obtained in a specific file. """

    if not file.endswith(AVAILABLE_EXTENCION):
        availables = ", ".join(AVAILABLE_EXTENCION)
        click.echo(
            formater(
                message=(
                    "Sorry the CLI does not support this extencion. "
                    f"Available extencions are {availables}."
                ),
                status=FormatterStatus.ERROR
            )
        )

    else:
        domain_parser(domain)

        rdap_api = RdapApi(domain)
        domain_data = rdap_api.get_domain_data()

        if file.endswith(TextFormatConstants.JSON):
            save_file_data(domain_data, file, _type=TextFormatConstants.JSON)

            click.echo(
                formater(message="Saved [{0}] {1}".format(
                    TextFormatConstants.JSON,
                    get_save_location(file)),
                    status=FormatterStatus.SUCCESS
                )
            )

        elif file.endswith(TextFormatConstants.TEXT):
            data = convert_into_txt(domain_data)
            save_file_data(data, file, _type=TextFormatConstants.TEXT)

            click.echo(
                formater(message="Saved [{0}] {1}".format(
                    TextFormatConstants.TEXT,
                    get_save_location(file)),
                    status=FormatterStatus.SUCCESS
                )
            )

        elif file.endswith(TextFormatConstants.YML):
            data = convert_into_yml(domain_data)
            save_file_data(data, file, _type=TextFormatConstants.YML)

            click.echo(
                formater(message="Saved [{0}] {1}".format(
                    TextFormatConstants.YML,
                    get_save_location(file)),
                    status=FormatterStatus.SUCCESS
                )
            )

def convert_into_txt(data:dict) -> str:
    """
    Used to simplify the text generator
    for .txt files.
    Args:
        data (dict): [Receive a result from the RdapApi query]
    Returns:
        str: [return a simple text available for .txt files]
    """

    tmp = []
    for key, value in data.items():
        field = f"{key}: {value}\n"
        tmp.append(field)
    _text = "".join(tmp)

    return _text

def convert_into_yml(data:dict) -> str:
    pass

def get_save_location(file_string:str) -> str:
    return f"{os.getcwd()}/{file_string}"

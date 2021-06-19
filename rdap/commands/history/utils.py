import click
from tabulate import tabulate
from typing import Union
from rdap.common.utils import (
    load_file_data
)
from rdap.common.constants import (
    MessageColors
)
from rdap.settings import (
    CACHE_FILE_PATH
)


def decorate(key:str, value:str) -> Union[dict,str]:
    """In charge of decorate the domain status column

    Args:
        key (str): [get the key from the context]
        value (str): [get the value from the context]

    Returns:
        str: [return a user-friendly status]
    """

    if isinstance(value, bool) and key == "status":
        if value:
            value = click.style("Available", fg=MessageColors.GREEN , bold=True)
        else:
            value = click.style("Taken", fg=MessageColors.RED, bold=True)

    elif isinstance(value, bool):
        if value:
            value = click.style("Yes", fg=MessageColors.GREEN , bold=True)
        else:
            value = click.style("No", fg=MessageColors.RED, bold=True)

    
    return value


def get_headers(history:list) -> list:
    """In charge of preparing the table headers.
    Only picks the element 0.

    Args:
        history (list): [this is a list with elements]

    Returns:
        list: [return a list with the elements to be show in the table as headers]
    """
    return [
        head.upper().replace("_", " ") for head in history[0] if not "content" in head
    ]


def get_content(history:list) -> list:
    """In charge of preparing the table rows.

    Args:
        history (list): [this is a list of dicts]

    Returns:
        list: [a list of lists ready to be show in the table]
    """

    body = []
    for objects in history:
        df = [
            decorate(key, value) for key, value in objects.items() if not "content" in key
        ]
        body.append(df)

    return body


def generate_table():
    """Just as the function says, generate a table based on the
    get_headers and get_content functions.

    Returns:
        [type]: [return a table]
    """
    try:
        history = load_file_data(CACHE_FILE_PATH)
    except FileNotFoundError:
        return click.echo(
            click.style(
                "[INFO] - There are no records available yet.",
                fg=MessageColors.YELLOW,
                bold=True,
            )
        )
    
    headers = get_headers(history)
    content = get_content(history)
    return click.echo(
        tabulate(
            content,
            headers,
            tablefmt="fancy_grid",
            stralign="center"
        )
    )


def get_record(id:str) -> dict:
    """In charge of get the specific ID passed from the context
    and return the payload related to it in the history json-file.

    Args:
        id ([str]): [description]

    Returns:
        [tuple[dict|str]]: [
            return a dict if the record was found or a string
            if not
        ]
    """

    try:
        _history = load_file_data(CACHE_FILE_PATH)    
    except FileNotFoundError:
        return click.echo(
            click.style(
                f"[ERROR] - {id} does not exist in your history. ¿Have you deleted it?",
                fg=MessageColors.RED,
                bold=True
            )
        )

    for record in _history:
        if str(id) == str(record["id"]):
            return record

    return click.echo(
        click.style(
            f"[ERROR] - Nothing was found to match with this '{id}'",
            fg=MessageColors.RED,
            bold=True,
        )
    )

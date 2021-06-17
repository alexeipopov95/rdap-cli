import click
from tabulate import tabulate
from rdap.common.utils import (
    load_file_data
)
from rdap.common.constants import (
    MessageColors
)
from rdap.settings import (
    CACHE_FILE_PATH
)

# TODO: Docstrings
def decorate(key, value):
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


# TODO: Docstrings
def get_headers(history:list) -> list:
    return [
        head.upper().replace("_", " ") for head in history[0] if not "content" in head
    ]

# TODO: Docstrings
def get_content(history:list) -> list:

    body = []
    for objects in history:
        df = [
            decorate(key, value) for key, value in objects.items() if not "content" in key
        ]
        body.append(df)

    return body

# TODO: Docstrings
def generate_table():
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


def get_record(id): # DOC STRINGS

    _history = load_file_data(CACHE_FILE_PATH)
    for record in _history:
        if str(id) == str(record["id"]):
            return record


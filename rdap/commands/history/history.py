import click
from rdap.commands.history.utils import (
    generate_table
)


@click.command()
def history():
    """ Return a table with the history of the
    lattest queryes """

    generate_table()

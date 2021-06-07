import click
from rdap.common.constants import (
    MessageColors,
)

HISTORY_RDAP_DETAIL = (
    "Show the detail about the requested search. "
    "You must pass the query_id."
)

@click.command()
@click.option("--detail", "detail_id", help=HISTORY_RDAP_DETAIL)
def history(detail_id:str) -> click.echo:
    """ Return a history of the last searches. """
    
    

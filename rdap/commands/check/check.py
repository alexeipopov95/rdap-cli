import click
from rdap.commands.gather.utils import domain_validator


@click.command()
@click.argument("domain", nargs=1)
def check(domain) -> None:
    """ Check if the domain is available or not. """
    domain_validator(domain)
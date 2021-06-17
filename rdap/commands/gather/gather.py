from rdap.common.constants import MessageColors
import click
from rdap.services.rdap import RdapApi
from rdap.commands.gather.utils import domain_validator
from rdap.common.utils import format_domain_output
from rdap.commands.gather.exceptions import (
    DomainWithSubdomain,
    DomainWithHttp,
    DomainValidationError,
)

# TODO Dont forget to make a strong domain validation
@click.command()
@click.argument("domain", nargs=1)
def gather(domain: str) -> None:
    """ Gather the domain information and prints in the shell.
    Give a valid domain name. In example: 'google.com', 'mydomain.net', etc.
    """

    try:
        domain_validator(domain)
    except (
        DomainWithSubdomain,
        DomainWithHttp,
        DomainValidationError
    ) as ex:
        return click.echo(
            click.style(
                f"[ERROR] {ex}",
                fg=MessageColors.RED,
                bold=True,
            )
    )

    schema = RdapApi(domain).query()
    message = format_domain_output(schema)

    click.echo(
        message
    )

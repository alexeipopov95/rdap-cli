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
from rdap.common.save import Save


@click.command()
@click.argument("domain", nargs=1)
@click.option(
    "-s",
    "--file",
    "filename",
    help=(
        "Give a file format and the result is going to be saved there. "
        "I.e 'my_file.json' or 'my_file.txt'"
    ),
)
def gather(domain: str, filename: str) -> None:
    """Gather the domain information and prints in the shell.
    Give a valid domain name. In example: 'google.com', 'mydomain.net', etc.
    """

    try:
        domain_validator(domain)
    except (DomainWithSubdomain, DomainWithHttp, DomainValidationError) as ex:
        return click.echo(
            click.style(
                f"[ERROR] {ex}",
                fg=MessageColors.RED,
                bold=True,
            )
        )

    schema = RdapApi(domain).query()

    if filename:
        return Save().save_harvest(filename, schema)

    message = format_domain_output(schema)

    click.echo(message)

import click
from rdap.services.rdap import RdapApi
from rdap.common.constants import MessageColors, DomainAvailability
from rdap.commands.gather.utils import domain_validator
from rdap.common.utils import form_hostname
from rdap.settings import UNDEFINED_DATA
from rdap.commands.gather.exceptions import (
    DomainWithSubdomain,
    DomainWithHttp,
    DomainValidationError,    
)

@click.command()
@click.argument("domain", nargs=1)
def check(domain) -> None:
    """ Check if the domain is available or not. """

    try:
        domain_validator(domain)
    except (
        DomainWithSubdomain,
        DomainWithHttp,
        DomainValidationError,
    ) as ex:
        return click.echo(
            click.style(
                f"[ERROR] {ex}",
                fg=MessageColors.RED,
                bold=True,
            )
    )

    schema = RdapApi(domain).query()

    if schema.get("status"):
        is_available = click.style(
            DomainAvailability.AVAILABLE,
            fg=DomainAvailability.availability_color_map.get(
                DomainAvailability.AVAILABLE
            ),
            bold=True
        )
    else:
        is_available = click.style(
            DomainAvailability.UNAVAILABLE,
            fg=DomainAvailability.availability_color_map.get(
                DomainAvailability.UNAVAILABLE
            ),
            bold=True
        )

    message = f"""
    Domain: {click.style(domain.upper(), MessageColors.WHITE, bold=True)}
    Status: {is_available}
    Rdap Host: {form_hostname(schema.get("query_host"))}
    Query host: {schema.get("query_host", UNDEFINED_DATA) or " - "}
    """
    click.echo(message)

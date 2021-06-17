import click
from rdap.services.rdap import RdapApi
from rdap.common.constants import MessageColors, DomainAvailability
from rdap.commands.gather.utils import domain_validator
from rdap.common.utils import (
    form_hostname,
    get_availability,
) 
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
    is_available = get_availability(schema)
    message = f"""
    Domain: {click.style(domain.upper(), MessageColors.WHITE, bold=True)}
    Status: {is_available}
    Rdap Host: {form_hostname(schema.get("query_host", UNDEFINED_DATA))}
    Query host: {schema.get("query_host", UNDEFINED_DATA)}
    """
    click.echo(message)

import click
from rdap.services.rdap import RdapApi
from rdap.common.constants import MessageColors, DomainAvailability
from rdap.commands.gather.utils import domain_validator
from rdap.commands.check.utils import form_hostname
from rdap.settings import UNDEFINED_DATA

@click.command()
@click.argument("domain", nargs=1)
def check(domain) -> None:
    """ Check if the domain is available or not. """

    domain_validator(domain)
    schema = RdapApi(domain).query()

    if schema.get("is_available"):
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
    Rdap Host: {form_hostname(schema.get("host"))}
    Query host: {schema.get("host", UNDEFINED_DATA)}
    """
    click.echo(message)

import click
from rdap.services.rdap import RdapApi
from rdap.commands.gather.utils import domain_validator
from rdap.common.constants import (
    MessageColors,
    DomainAvailability
)

# TODO Dont forget to make a strong domain validation
@click.command()
@click.argument("domain", nargs=1)
def gather(domain: str) -> None:
    """ Gather the domain information and prints in the shell.
    Give a valid domain name. In example: 'google.com', 'mydomain.net', etc.
    """

    domain_validator(domain)
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
    
    schema = schema["content"]
    dns = " \n\t\t    ".join(schema.get("dns").split(","))
    message = f"""
        Domain: {
            click.style(schema.get("domain").upper(), fg=MessageColors.WHITE, bold=True)
        }
        Status: {is_available}

        Nameservers: {
            click.style(dns, fg=MessageColors.WHITE, bold=True)
        }

        Create date: {
            click.style(schema.get("create_at"), fg=MessageColors.WHITE, bold=True)
        }
        Expire date: {
            click.style(schema.get("expire_at"), fg=MessageColors.WHITE, bold=True)
        }
        Update date: {
            click.style(schema.get("update_at"), fg=MessageColors.WHITE, bold=True)
        }
        Update date (RDAP): {
            click.style(schema.get("updata_at_rdap"), fg=MessageColors.WHITE, bold=True)
        }

        Entity: {
            click.style(schema.get("entity"), fg=MessageColors.WHITE, bold=True)
        }
        Name: {
            click.style(schema.get("name"), fg=MessageColors.WHITE, bold=True)
        }
        Registrant ID: {
            click.style(schema.get("registrant_id"), fg=MessageColors.WHITE, bold=True)
        }

    """
    click.echo(message)

    
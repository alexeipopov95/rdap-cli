import rdap
import click

from rdap.utils.rdap_api import RdapApi
from rdap.utils.utils import (
    domain_validator,
)
from rdap.commands.exceptions import (
    GatherEmptyParam,
    GatherInvalidDomainName
)
from rdap.common.constants import (
    MessageColors,
)

GATHER_RDAP_HELP = "The domain name. I.e 'google.com'"

@click.command()
@click.option("--domain", help=GATHER_RDAP_HELP)
def gather(domain: str) -> None:
    """
    Command in charge of gathering a certain domain info
    and just show it as an console output in a human readable form

    Args:
        domain (str): [valid domain name to being query]
    """

    if not domain:
        raise GatherEmptyParam(
            f"Domain was {domain}, please provide a valid domain using --domain option"
        )

    if not domain_validator(domain):
        raise GatherInvalidDomainName(
            f"Domain '{domain}' is not a valid domain name."
        )
    
    rdap_api = RdapApi(domain).get_domain_data()

    if rdap_api:
        message = f"""
        Domain: {click.style(text=domain, fg=MessageColors.GREEN, bold=True)}
        Nameservers: {click.style(text=rdap_api.get("dns"), fg=MessageColors.GREEN, bold=True)}
        Creation date: {click.style(text=rdap_api.get("created_at"), fg=MessageColors.GREEN, bold=True)}
        Expiration date: {click.style(text=rdap_api.get("expire_at"), fg=MessageColors.GREEN, bold=True)}
        Last updated: {click.style(text=rdap_api.get("update_at"), fg=MessageColors.GREEN, bold=True)}
        Last updated in RDAP: {click.style(text=rdap_api.get("update_at_rdap"), fg=MessageColors.GREEN, bold=True)}
        Entity: {click.style(text=rdap_api.get("entity"), fg=MessageColors.GREEN, bold=True)}
        ID: {click.style(text=rdap_api.get("id"), fg=MessageColors.GREEN, bold=True)}
        Owner: {click.style(text=rdap_api.get("name"), fg=MessageColors.GREEN, bold=True)}
        """
        click.echo(message)

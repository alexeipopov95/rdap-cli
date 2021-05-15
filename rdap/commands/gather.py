import click

from rdap.utils.rdap_api import RdapApi
from rdap.utils.utils import (
    formater,
    domain_validator,
)
from rdap.common.exceptions import (
    GatherEmptyParam,
    GatherInvalidDomainName
)
from rdap.common.constants import (
    FormatterStatus,
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
    
    rdap = RdapApi(domain=domain)
    print(rdap.get_domain_data(domain))
    

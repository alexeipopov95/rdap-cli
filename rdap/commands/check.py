import click
import time
from rdap.utils.rdap_api import RdapApi
from rdap.utils.utils import domain_parser, file_parser, formater
from rdap.common.constants import FormatterStatus


CHECK_RDAP_HELP = ""
CHECK_RDAP_HELP_FILE = ""

@click.command()
@click.option(
    "--domain",
    help=CHECK_RDAP_HELP,
)
@click.option(
    "--file",
    help=CHECK_RDAP_HELP_FILE,
)
@click.option(
    "--sleep",
    default=3,
    help=CHECK_RDAP_HELP_FILE,
)
def check(**kwargs) -> None:
    """ Check if the domain is available or not. """
    domain = kwargs.get("domain")
    file = kwargs.get("file")
    sleep = kwargs.get("sleep")

    if domain:
        domain = domain_parser(domain)
        is_available = RdapApi(domain).get_domain_data()

        if is_available:
            click.echo(
                formater(
                    f"{domain.upper()} it is not available.",
                    status=FormatterStatus.ERROR
                )
            )

    elif file:
        file = file_parser(file)

        for domain in file:
            try:
                is_available = RdapApi(domain).get_domain_data()
                if is_available:
                    click.echo(
                        formater(
                            f"{domain.upper()} it is not available.",
                            status=FormatterStatus.ERROR
                        )
                    )
            except Exception as ex:
                print(ex)

            time.sleep(sleep)

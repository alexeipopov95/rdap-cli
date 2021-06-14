import click
import time
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
    file = kwargs.get("file", None)
    sleep = kwargs.get("sleep")

    if domain:
        domain = domain_parser(domain)
        not_available = RdapApi(domain).get_domain_data()

        if not_available:
            click.echo(
                formater(
                    f"{domain} it is not available.",
                    status=FormatterStatus.ERROR
                )
            )

    elif file:
        file = file_parser(file)

        for domain in file:
            try:
                not_available = RdapApi(domain).get_domain_data()
                if not_available:
                    click.echo(
                        formater(
                            f"{domain} it is not available.",
                            status=FormatterStatus.ERROR
                        )
                    )
            except Exception as ex:
                print(ex)

            time.sleep(sleep)
    else:
        valid_options = ", ".join([f"--{opt}" for opt in kwargs]) 
        click.echo(
            formater(
                message=(
                    "You have to pass a valid option. "
                    "This are the valid options: "
                    f"{valid_options}"
                ), status=FormatterStatus.ERROR
            )
        )

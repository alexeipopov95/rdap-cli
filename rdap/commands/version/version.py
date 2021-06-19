import click
import pkg_resources
from rdap.common.constants import MessageColors


@click.command(name="version")
def version():
    """
    Show the project version.
    """

    version = pkg_resources.require("rdap-cli")[0].version
    click.echo(click.style(str(version), fg=MessageColors.YELLOW, bold=True))

import click
import pkg_resources
from rdap.common.utils import formater
from rdap.common.constants import AlertTagMessage


@click.command(name="version")
def version():
    """
    Show the project version.
    """

    version = pkg_resources.require("rdap-cli")[0].version
    return formater(f"Rdap CLI version: {version}", AlertTagMessage.INFO)

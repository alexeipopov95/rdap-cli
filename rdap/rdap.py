import click
from rdap.services.rdap import RdapApi

COMMAND_LIST = [
    "gather",
    "history",
    "check",
]


@click.command()
@click.option(
    "--domain",
)

def mi_test(domain):
    api = RdapApi(domain)
    a = api.query()


@click.group()
def cli() -> None:
    pass

cli.add_command(mi_test)

if __name__ == "__main__":
    cli()

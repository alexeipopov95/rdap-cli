from rdap.commands.gather import gather
from rdap.commands.history import history
from rdap.commands.check import check

import click

@click.group()
def cli() -> None:
    pass

cli.add_command(gather)
cli.add_command(history)
cli.add_command(check)

if __name__ == "__main__":
    cli()

import click
from rdap.commands.gather import gather
from rdap.commands.history import history
from rdap.commands.check import check
from rdap.commands.version import version
from rdap.commands.settings import settings



@click.group()
@click.pass_context
def cli(ctx) -> None:
    pass

cli.add_command(gather)
cli.add_command(check)
cli.add_command(history)
cli.add_command(version)
cli.add_command(settings)

if __name__ == "__main__":
    cli()

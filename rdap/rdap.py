import click
from rdap.commands.check import check
from rdap.commands.gather import gather
from rdap.commands.save import save
from rdap.commands.history import history


@click.group()
def cli() -> None:
    pass


cli.add_command(gather)
cli.add_command(save)
cli.add_command(check)
cli.add_command(history)

if __name__ == "__main__":
    cli()

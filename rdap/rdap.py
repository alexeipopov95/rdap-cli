import click
from rdap.commands.check import check
from rdap.commands.gather import gather
from rdap.commands.save import save


@click.group()
def cli() -> None:
    pass


cli.add_command(gather)
cli.add_command(save)
cli.add_command(check)

if __name__ == "__main__":
    cli()

import click
from rdap.commands.gather import gather
from rdap.commands.save import save


@click.group()
def cli() -> None:
    pass


cli.add_command(gather)
cli.add_command(save)

if __name__ == "__main__":
    cli()

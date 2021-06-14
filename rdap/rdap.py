from rdap.commands.gather import gather
import click

COMMAND_LIST = [
    "gather",
    "history",
    "check",
]


@click.group()
def cli() -> None:
    pass

cli.add_command(gather)

if __name__ == "__main__":
    cli()

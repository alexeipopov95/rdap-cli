import os
import click
from rdap.settings import CACHE_FILE_PATH
from rdap.commands.history.utils import (
    get_record,
    generate_table,
)
from rdap.common.utils import (
    format_domain_output,
    load_file_data,
)
from rdap.common.constants import (
    MessageColors,
)
from rdap.common.save import Save


@click.group(name="history", invoke_without_command=True)
@click.pass_context
def history(ctx):
    """Returns a table with the history of the last searches."""

    if ctx.invoked_subcommand is None:
        generate_table()


@history.command(name="detail")
@click.argument("id")
def detail(id):
    """Returns the detail of the specific ID."""

    output = get_record(id)
    if output:
        message = format_domain_output(output)
        click.echo(message)


@history.command(name="clear")
def clear():
    """Clean history."""

    try:
        os.remove(CACHE_FILE_PATH)
    except FileNotFoundError:
        return click.echo(
            click.style(
                "[INFO] - You have no history to delete.",
                fg=MessageColors.YELLOW,
                bold=True,
            )
        )

    click.echo(
        click.style(
            "[DONE] - History was cleaned.",
            fg=MessageColors.GREEN,
            bold=True,
        )
    )


@history.command(name="download")
@click.argument("filename")
def download(filename):
    """Download the history into a file."""

    try:
        _history = load_file_data(CACHE_FILE_PATH)
    except FileNotFoundError:
        return click.echo(
            click.style(
                "[INFO] - Nothing to download.",
                fg=MessageColors.YELLOW,
                bold=True,
            )
        )

    Save().save_harvest(filename, _history)

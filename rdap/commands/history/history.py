import click
from rdap.commands.history.utils import (
    get_record,
    generate_table,
)
from rdap.common.utils import (
    format_domain_output,
)
from rdap.common.constants import (
    MessageColors,
)

@click.group(name="history", invoke_without_command=True)
@click.pass_context
def history(ctx):
    """ Return a table with the history of the
    lattest queryes. """

    if ctx.invoked_subcommand is None:
        generate_table()


@history.command(name="detail")
@click.argument("id")
def detail(id):
    
    output = get_record(id)
    
    if not output:
        return click.echo(
            click.style(
                f"Nothing was found to match with this '{id}'",
                fg=MessageColors.RED,
                bold=True,
            )
        )
    
    message = format_domain_output(output)

    click.echo(
        message
    )

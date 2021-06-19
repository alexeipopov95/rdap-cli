from rdap.common.constants import MessageColors
import click

@click.group(name="settings", invoke_without_command=True)
@click.pass_context
def settings(ctx):
    """ Print the CLI settings. """

    if ctx.invoked_subcommand is None:
        print("SETTINGS WIP")


@settings.command()
def set():
    """
    Modify some params of the CLI
    """
    print("SET WIP")

@settings.command()
def show():
    """
    Show the available params of the CLI.
    Their status and values.
    """    
    print("SHOW WIP")
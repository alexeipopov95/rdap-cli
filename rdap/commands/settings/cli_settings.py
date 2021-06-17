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
    print("SET WIP")

@settings.command()
def show():
    print("SHOW WIP")
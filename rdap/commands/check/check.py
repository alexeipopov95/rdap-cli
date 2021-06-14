import click


@click.command()
@click.argument("domain", nargs=1)
def check(domain) -> None:
    """ Check if the domain is available or not. """

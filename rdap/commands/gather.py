import click

GATHER_RDAP_HELP = "The domain name. I.e 'google.com'"

@click.command()
@click.option("--domain", help=GATHER_RDAP_HELP)
def gather(domain: str) -> None:
    """
    command in charge of gathering a certain domain info
    and just show it as an console output in a human readable form

    Args:
        domain (str): [valid domain name to being query]
    """
    click.echo(
        "Gathering information about {0}...".format(domain)
    )

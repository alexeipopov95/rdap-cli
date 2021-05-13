import click

# help texts
GATHER_RDAP = "The domain name. I.e 'google.com'"


@click.group()
def rdap() -> None:
    pass

@rdap.command()
@click.option("--domain", help=GATHER_RDAP)
def gather(domain: str) -> None:
    click.echo(
        "Gathering information about {0}...".format(domain)
    )

@rdap.command()
def save() -> None:
    click.echo("Saving...")


if __name__ == "__main__":
    rdap()
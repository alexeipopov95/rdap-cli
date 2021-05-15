import click


SAVE_RDAP_HELP = (
    "You can specify the file name where you want to save the info. "
    "It will save the file on your current working directory i.e: "
    "--file=result.txt or --file=result.json"
)

@click.command()
@click.option("--domain")
@click.option("--file", help=SAVE_RDAP_HELP)
def save(domain=None, file="result.txt") -> None:
    """
    Save the respective domain query into a file
    """
    click.echo("Saving...")
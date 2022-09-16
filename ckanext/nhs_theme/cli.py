import click


@click.group(short_help="nhs_theme CLI.")
def nhs_theme():
    """nhs_theme CLI.
    """
    pass


@nhs_theme.command()
@click.argument("name", default="nhs_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [nhs_theme]

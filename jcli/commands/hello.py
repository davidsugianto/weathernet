import click

@click.command()
@click.argument('name', nargs=1)
def hello(name):
    """
    simple command thats say hello
    """
    click.echo(f'Hello {name}')
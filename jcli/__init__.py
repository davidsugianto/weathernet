"""Top-level package for CLI App"""
import click
from jcli import commands

__author__="""David Sugianto"""
__email__='idiots718@gmail.com'
__version__='0.1'

@click.group()
def cli():
    pass

# Add Commands
cli.add_command(commands.hello)
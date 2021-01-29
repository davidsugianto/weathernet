import click
import os
import sys
from .commands import check
from .commands import build
from .commands import deploy

@click.group(help="jcli is a jogjacode CLI tools for automation using python + ansible")
def cli():
    pass

cli.add_command(check.check)
cli.add_command(build.build)
cli.add_command(deploy.deploy)

if __name__ == "__main__":
    cli()
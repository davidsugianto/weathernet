import click

@click.command(help='command directive for build docker image')
@click.option('--docker', '-d', is_flag=True, help='Indicates the project should be built into docker image')
def build(docker):
    if docker:
        print(f'Building this repo into a docker image')
    else:
        print(f'Building this repo using default method')
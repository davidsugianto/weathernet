import click

@click.command(help='command directive for health check to server in env')
@click.option('--env', '-e', default="dev", type=click.Choice(['dev', 'staging', 'production'], case_sensitive=False), prompt='Enter env name to server health check', help='Env to health check')
@click.option('--server', '-s', prompt='Enter the server hostname', help='Server destination to health check')
def check(env,server):
    print(f'Server health check {server} in a {env} environment')
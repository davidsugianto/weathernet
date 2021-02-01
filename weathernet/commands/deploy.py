import click

@click.command(help='command directive for deploy to multiple cloud and multiple env')
@click.option('--env', '-e', default="dev", type=click.Choice(['dev', 'staging', 'production'], case_sensitive=False), prompt='Enter env name to deploy', help='Env to deploy')
@click.option('--cloud', '-c', default="aws", type=click.Choice(['aws', 'gcp', 'azure'], case_sensitive=False), prompt='Enter cloud to deploy', help='Cloud to deploy')
def deploy(env, cloud):
    print(f'Deploying current application artifact to {env} environment in {cloud} cloud')
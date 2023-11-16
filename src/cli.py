import click
from iaas.opentack_connector import OpenstackConnector

@click.group()
def cli():
    pass


@click.command()
@click.option('--timeout', default=12, help='Timeout for API calls in seconds')
@click.argument('cloud')
def openstack(cloud, timeout):
    """Generates Gaia-X Credentials for openstack cloud CLOUD.
    CLOUD MUST refer to a name defined in Openstack's configuration file clouds.yaml."""

    conn = OpenstackConnector(cloud, timeout=timeout)



@click.command()
def kubernetes():
    """Generates Gaia-X Credentials for kubernetes."""
    pass


cli.add_command(openstack)
cli.add_command(kubernetes)

if __name__ == '__main__':
    cli()

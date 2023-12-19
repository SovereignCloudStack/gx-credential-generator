import click
import openstack as os
import sys
import yaml

from generator.discovery.openstack.opentack_discovery import OsCloud


@click.group()
def cli():
    pass


@click.command()
@click.option('--config', default='../config/config.yaml', help='Path to Configuration file for SCS GX Credential Generator.')
@click.option('--timeout', default=12, help='Timeout for API calls in seconds')
@click.argument('cloud')
def openstack(cloud, timeout, config):
    """Generates Gaia-X Credentials for openstack cloud CLOUD.
    CLOUD MUST refer to a name defined in Openstack's configuration file clouds.yaml."""

    # init Openstack Connections
    conn = os.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4)
    try:
        conn.authorize()
    except Exception:
        print("INFO: Retry connection with 'default' domain", file=sys.stderr)
        conn = os.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4,
                                 default_domain='default', project_domain_id='default')
        conn.authorize()

    # generate Gaia-X Credentials
    with open(config, "r") as config_file:
        os_cloud = OsCloud(conn, yaml.safe_load(config_file))
        props = os_cloud.discover_properties()


@click.command()
def kubernetes():
    """Generates Gaia-X Credentials for kubernetes."""
    pass


cli.add_command(openstack)
cli.add_command(kubernetes)

if __name__ == '__main__':
    cli()

import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('cloud')
def openstack(cloud):
    """Generates Gaia-X Credentials for openstack cloud CLOUD.
    CLOUD MUST refer to a name defined in Openstack's configuration file clouds.yaml."""
    click.echo(f"Hello {cloud}!")


@click.command()
def kubernetes():
    """Generates Gaia-X Credentials for kubernetes."""
    pass


cli.add_command(openstack)
cli.add_command(kubernetes)


if __name__ == '__main__':
    cli()


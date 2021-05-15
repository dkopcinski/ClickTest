import click

@click.command()
@click.option('--name', default='Dawid', help='Your name for the greeting')
def cli(name):
    """Example script."""
    click.echo(f'Hello {name} !!!')

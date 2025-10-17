"""
Command-line interface for MedeX
Uses Click for CLI functionality
"""

import click
from medex import __version__
from medex.app import run_once
from medex.config import get_mode, get_config


@click.group()
@click.version_option(version=__version__, prog_name="medex")
def cli():
    """MedeX - AI-powered Clinical Reasoning Assistant"""
    pass


@cli.command()
@click.option(
    "--mode",
    type=click.Choice(["mock", "educational", "professional"]),
    help="Operation mode",
)
@click.option(
    "--query",
    "-q",
    required=True,
    help="Medical query to process",
)
def query(mode, query):
    """Process a medical query"""
    try:
        response = run_once(query, mode=mode)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@cli.command()
def config():
    """Show current configuration"""
    cfg = get_config()
    click.echo(f"Mode: {cfg['mode']}")
    click.echo(f"API Key configured: {cfg['has_api']}")


@cli.command()
def info():
    """Show system information"""
    click.echo(f"MedeX v{__version__}")
    click.echo(f"Current mode: {get_mode()}")


if __name__ == "__main__":
    cli()

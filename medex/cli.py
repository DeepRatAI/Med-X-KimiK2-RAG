import click
from medex.app import run_once

@click.command()
@click.option("--mode", type=click.Choice(["educational","pro"]), default="educational")
@click.option("--query", prompt=True, help="Pregunta clínica")
def main(mode, query):
    print(run_once(query, mode))

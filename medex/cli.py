"""
MedeX Command Line Interface.

Provides a CLI tool to interact with the MedeX medical AI system.
"""
import click
from medex.app import run_once


@click.command()
@click.option(
    "--mode",
    type=click.Choice(["educational", "professional"], case_sensitive=False),
    default="educational",
    help="Query mode: educational for learning, professional for clinical cases"
)
@click.option(
    "--query",
    type=str,
    required=True,
    help="Medical query to process"
)
def main(mode: str, query: str):
    """
    MedeX - AI-Powered Clinical Reasoning Assistant (Educational Prototype)
    
    Process medical queries using the MedeX system with RAG capabilities.
    
    Examples:
    
        medex --mode educational --query "¿Qué es la diabetes?"
        
        medex --mode professional --query "Paciente con dolor torácico"
    """
    try:
        print(f"🏥 MedeX v0.1.0 - Processing query...")
        print(f"📋 Mode: {mode}")
        print(f"❓ Query: {query}")
        print("-" * 60)
        
        response = run_once(query, mode=mode)
        
        print("\n" + "=" * 60)
        print("📝 Response:")
        print("=" * 60)
        print(response)
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise click.Abort()


if __name__ == "__main__":
    main()


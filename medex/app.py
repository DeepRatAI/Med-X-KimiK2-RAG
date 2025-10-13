"""
MedeX application module.

Provides high-level functions to run medical queries through the MedeX system.
"""
from medex.adapters import build_pipeline, answer_query


def run_once(query: str, mode: str = "educational") -> str:
    """
    Run a single medical query through MedeX and return the response.
    
    Args:
        query: The medical query to process
        mode: Query mode - "educational" for learning, "professional" for clinical cases
              (Note: MedeX auto-detects user type, but mode provides a hint)
    
    Returns:
        str: The generated medical response
    
    Example:
        >>> response = run_once("¿Qué es la diabetes?", mode="educational")
        >>> print(response)
    """
    pipe = build_pipeline()
    return answer_query(pipe, query=query, mode=mode)


"""
Main application module for MedeX
Provides core query processing functionality
"""

from typing import Optional
from medex.config import get_mode, get_api_key
from medex.adapters import build_pipeline, answer_query


def run_once(query: str, mode: Optional[str] = None) -> str:
    """
    Process a single query and return the response.
    
    This is the main entry point for the MedeX application.
    Works in mock mode without API keys.
    
    Args:
        query: Medical query to process
        mode: Optional mode override ('mock', 'educational', 'professional')
    
    Returns:
        Response string
    """
    # Determine mode
    if mode is None:
        mode = get_mode()
    
    # Build pipeline (returns None in mock mode)
    pipeline = build_pipeline(mode)
    
    # Get answer
    response = answer_query(pipeline, query, mode)
    
    return response

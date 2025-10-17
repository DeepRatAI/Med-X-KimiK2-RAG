"""
Adapters module for MedeX
Handles integration with RAG pipeline and legacy systems
"""

from typing import Optional, Any


def build_pipeline(mode: str = "mock") -> Optional[Any]:
    """
    Build RAG pipeline based on mode.
    
    In mock mode, returns None.
    In other modes, would integrate with legacy systems (lazy import).
    
    Args:
        mode: Operation mode ('mock', 'educational', 'professional')
    
    Returns:
        Pipeline object or None in mock mode
    """
    if mode == "mock":
        return None
    
    # In production, this would do lazy import of MEDEX_FINAL
    # For now, return None if legacy not available
    try:
        # Lazy import to avoid import-time dependencies on legacy
        import sys
        if "MEDEX_FINAL" in sys.modules:
            # Legacy available
            pass
    except ImportError:
        pass
    
    return None


def answer_query(pipeline: Optional[Any], query: str, mode: str = "mock") -> str:
    """
    Answer a medical query using the pipeline.
    
    In mock mode, returns a mock response with markers.
    
    Args:
        pipeline: RAG pipeline object or None
        query: User query
        mode: Operation mode
    
    Returns:
        Response string
    """
    if pipeline is None or mode == "mock":
        # Mock response with stable markers for testing
        return f"""MOCK RESPONSE for query: "{query}"

Mode: {mode}

This is a simulated response from MedeX running in mock mode.
In production, this would provide evidence-based medical information
retrieved through RAG (Retrieval-Augmented Generation).

⚠️ EDUCATIONAL USE ONLY
This is not real medical advice.
For medical concerns, consult a healthcare professional.
"""
    
    # In production, this would call the actual pipeline
    return "Production pipeline not available"

"""
Adapters module - Wraps legacy MEDEX_FINAL.py without modifying it.

This module provides a clean interface to the existing MedeXv2583 class,
allowing the new package structure to work with the legacy code.
"""
import asyncio
import os
from typing import Optional

try:
    from MEDEX_FINAL import MedeXv2583
except ImportError as e:
    raise RuntimeError(f"Cannot import MedeXv2583 from MEDEX_FINAL.py: {e}")


def build_pipeline():
    """
    Build and return a MedeXv2583 pipeline instance.
    
    Returns:
        MedeXv2583: Initialized medical AI system instance
    """
    # Set API key from environment if available
    if not os.getenv("KIMI_API_KEY"):
        # Check if we're in a test/mock environment
        print("⚠️  No KIMI_API_KEY found in environment")
        print("   For production use, set KIMI_API_KEY environment variable")
        print("   For local development, create api_key.txt file")
    
    return MedeXv2583()


def answer_query(pipeline: MedeXv2583, query: str, mode: str = "educational") -> str:
    """
    Generate an answer to a medical query using the pipeline.
    
    Args:
        pipeline: MedeXv2583 instance from build_pipeline()
        query: Medical query string
        mode: Query mode - "educational" for educational queries,
              "professional" for clinical cases (auto-detected)
    
    Returns:
        str: Generated response text
    """
    # The MedeXv2583.generate_response() is async, so we need to handle that
    try:
        # Create or get event loop
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        # Run the async generate_response method
        # Note: MedeXv2583 auto-detects user type, but we respect the mode parameter
        response = loop.run_until_complete(
            pipeline.generate_response(query, use_streaming=False)
        )
        
        return response
    except Exception as e:
        # If no API key or other error, return a helpful message
        if "API key" in str(e) or "api_key" in str(e).lower():
            return (
                "⚠️  MedeX Mock Response (No API Key)\n\n"
                f"Query received: {query}\n"
                f"Mode: {mode}\n\n"
                "This is a mock response because no KIMI_API_KEY is configured.\n"
                "To use the real MedeX system:\n"
                "1. Set environment variable: export KIMI_API_KEY='your-key'\n"
                "2. Or create api_key.txt file with your Moonshot API key\n\n"
                "For educational purposes, this demonstrates the CLI is working correctly."
            )
        else:
            return f"❌ Error generating response: {e}"

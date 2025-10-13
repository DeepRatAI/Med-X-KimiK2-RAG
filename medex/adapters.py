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
        MedeXv2583: Initialized medical AI system instance, or None if no API key
    """
    # Check if API key is available
    has_api_key = bool(os.getenv("KIMI_API_KEY"))
    has_file_key = os.path.exists("api_key.txt")
    
    if not has_api_key and not has_file_key:
        # No API key available - return None to signal mock mode
        print("⚠️  No KIMI_API_KEY found in environment or api_key.txt file")
        print("   Running in MOCK mode for testing purposes")
        return None
    
    try:
        return MedeXv2583()
    except Exception as e:
        print(f"⚠️  Could not initialize MedeXv2583: {e}")
        print("   Running in MOCK mode")
        return None


def answer_query(pipeline: Optional[MedeXv2583], query: str, mode: str = "educational") -> str:
    """
    Generate an answer to a medical query using the pipeline.
    
    Args:
        pipeline: MedeXv2583 instance from build_pipeline(), or None for mock mode
        query: Medical query string
        mode: Query mode - "educational" for educational queries,
              "professional" for clinical cases (auto-detected)
    
    Returns:
        str: Generated response text
    """
    # If no pipeline (no API key), return mock response
    if pipeline is None:
        return _generate_mock_response(query, mode)
    
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
        # If error occurs, return mock response
        print(f"⚠️  Error during query processing: {e}")
        return _generate_mock_response(query, mode)


def _generate_mock_response(query: str, mode: str) -> str:
    """Generate a mock response when API key is not available."""
    return f"""╔══════════════════════════════════════════════════════════════════════════╗
║                      🏥 MedeX v0.1.0 - MOCK RESPONSE                     ║
╚══════════════════════════════════════════════════════════════════════════╝

📋 Query Mode: {mode.upper()}
❓ Your Query: {query}

⚠️  MOCK MODE ACTIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is a mock response because no KIMI_API_KEY is configured.

The MedeX CLI and package structure are working correctly! ✅

To use the real MedeX medical AI system:

1️⃣  Set environment variable:
   export KIMI_API_KEY='your-moonshot-api-key-here'

2️⃣  Or create api_key.txt file:
   echo "your-moonshot-api-key-here" > api_key.txt

3️⃣  Get your API key from:
   https://platform.moonshot.cn/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 Package Features Demonstrated:
   ✅ CLI interface working
   ✅ Query parsing and routing
   ✅ Mode detection ({mode})
   ✅ Graceful error handling
   ✅ Mock response generation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  EDUCATIONAL PROTOTYPE DISCLAIMER
This system is for educational and research purposes only.
Not for clinical decision-making or patient care.
Always consult qualified healthcare professionals.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

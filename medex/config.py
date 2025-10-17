"""
Configuration module for MedeX
Handles environment variables and mode detection
"""

import os
from typing import Optional


def get_api_key() -> Optional[str]:
    """Get KIMI API key from environment"""
    return os.environ.get("KIMI_API_KEY", "")


def get_mode() -> str:
    """
    Get operation mode from environment.
    Returns: 'mock', 'educational', or 'professional'
    """
    mode = os.environ.get("MEDEX_MODE", "educational").lower()
    valid_modes = ["mock", "educational", "professional"]
    if mode not in valid_modes:
        mode = "educational"
    
    # If no API key, force mock mode
    if not get_api_key():
        mode = "mock"
    
    return mode


def get_config() -> dict:
    """Get full configuration dictionary"""
    return {
        "api_key": get_api_key(),
        "mode": get_mode(),
        "has_api": bool(get_api_key()),
    }

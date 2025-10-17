"""
MedeX - Medical AI Assistant Package
Modular clinical reasoning assistant with RAG capabilities
"""

__version__ = "0.1.0"
__author__ = "DeepRatAI"
__description__ = "AI-powered Clinical Reasoning Assistant"

# Public API
from medex.config import get_config, get_mode
from medex.app import run_once

__all__ = [
    "__version__",
    "get_config",
    "get_mode",
    "run_once",
]

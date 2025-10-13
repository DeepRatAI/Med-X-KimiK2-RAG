"""
Configuration module for MedeX package.

Reads configuration from environment variables:
- KIMI_API_KEY: API key for Moonshot AI (Kimi)
- MEDEX_MODE: Default mode (educational or professional)
"""
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Application settings loaded from environment variables."""
    
    kimi_api_key: str = os.getenv("KIMI_API_KEY", "")
    mode_default: str = os.getenv("MEDEX_MODE", "educational")
    
    def __post_init__(self):
        """Validate settings after initialization."""
        if self.mode_default not in ("educational", "professional"):
            object.__setattr__(self, "mode_default", "educational")


# Global settings instance
settings = Settings()


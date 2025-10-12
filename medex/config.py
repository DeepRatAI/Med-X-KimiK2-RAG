from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    kimi_api_key: str = os.getenv("KIMI_API_KEY", "")
    mode_default: str = os.getenv("MEDEX_MODE", "educational")

settings = Settings()

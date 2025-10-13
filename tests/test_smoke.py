"""
Smoke test for MedeX package.

Basic tests to ensure the package is properly installed and working.
"""
import pytest
from medex.app import run_once


def test_import_medex():
    """Test that medex package can be imported."""
    import medex
    assert hasattr(medex, "__version__")
    assert medex.__version__ == "0.1.0"


def test_run_once_returns_text():
    """Test that run_once returns text response."""
    # Use a simple educational query
    query = "¿Qué es la diabetes?"
    mode = "educational"
    
    response = run_once(query, mode=mode)
    
    # Should return a string
    assert isinstance(response, str)
    # Should not be empty
    assert len(response) > 0
    # Should contain some text (even if it's a mock response)
    assert len(response.strip()) > 10


def test_run_once_professional_mode():
    """Test that run_once works with professional mode."""
    query = "Paciente con dolor torácico"
    mode = "professional"
    
    response = run_once(query, mode=mode)
    
    assert isinstance(response, str)
    assert len(response) > 0


def test_adapters_can_build_pipeline():
    """Test that adapters can build a pipeline."""
    from medex.adapters import build_pipeline
    
    pipeline = build_pipeline()
    
    # In mock mode (no API key), pipeline can be None
    # In real mode (with API key), it should be a MedeXv2583 instance
    if pipeline is not None:
        # Check it has expected methods
        assert hasattr(pipeline, "generate_response")
        assert hasattr(pipeline, "detect_user_type")
    else:
        # Mock mode is acceptable for testing
        # Just verify the function doesn't crash
        assert True


def test_config_settings():
    """Test that config settings are accessible."""
    from medex.config import settings
    
    # Should have the expected attributes
    assert hasattr(settings, "kimi_api_key")
    assert hasattr(settings, "mode_default")
    # Default mode should be educational
    assert settings.mode_default in ("educational", "professional")

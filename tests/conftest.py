"""
Pytest configuration and fixtures for medex tests
"""

import os
import sys
import pytest


@pytest.fixture
def no_api_no_legacy(monkeypatch):
    """
    Fixture that forces mock mode by:
    - Clearing KIMI_API_KEY
    - Removing MEDEX_FINAL from sys.modules if present
    """
    # Clear API key
    monkeypatch.delenv("KIMI_API_KEY", raising=False)
    monkeypatch.setenv("MEDEX_MODE", "mock")
    
    # Remove legacy from sys.modules if present
    if "MEDEX_FINAL" in sys.modules:
        del sys.modules["MEDEX_FINAL"]
    
    yield
    
    # Cleanup is handled by monkeypatch automatically


@pytest.fixture
def mock_mode(monkeypatch):
    """Fixture to set mock mode explicitly"""
    monkeypatch.setenv("MEDEX_MODE", "mock")
    monkeypatch.delenv("KIMI_API_KEY", raising=False)
    yield


@pytest.fixture
def educational_mode(monkeypatch):
    """Fixture to set educational mode"""
    monkeypatch.setenv("MEDEX_MODE", "educational")
    monkeypatch.delenv("KIMI_API_KEY", raising=False)
    yield


@pytest.fixture
def with_api_key(monkeypatch):
    """Fixture to set a dummy API key"""
    monkeypatch.setenv("KIMI_API_KEY", "sk-test-dummy-key-for-testing-only")
    yield

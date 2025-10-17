"""
Test configuration module
"""

import pytest
from medex.config import get_api_key, get_mode, get_config


def test_get_api_key_default(no_api_no_legacy):
    """Test API key retrieval with no key set"""
    key = get_api_key()
    assert key == ""


def test_get_api_key_with_key(with_api_key):
    """Test API key retrieval with key set"""
    key = get_api_key()
    assert key == "sk-test-dummy-key-for-testing-only"


def test_get_mode_default(no_api_no_legacy):
    """Test mode defaults to mock when no API key"""
    mode = get_mode()
    assert mode == "mock"


def test_get_mode_mock_explicit(mock_mode):
    """Test explicit mock mode"""
    mode = get_mode()
    assert mode == "mock"


def test_get_mode_educational(educational_mode):
    """Test educational mode without API key forces mock"""
    mode = get_mode()
    assert mode == "mock"  # Should force mock due to no API key


def test_get_mode_educational_with_api(monkeypatch):
    """Test educational mode with API key"""
    monkeypatch.setenv("MEDEX_MODE", "educational")
    monkeypatch.setenv("KIMI_API_KEY", "sk-test-key")
    mode = get_mode()
    assert mode == "educational"


def test_get_mode_professional_with_api(monkeypatch):
    """Test professional mode with API key"""
    monkeypatch.setenv("MEDEX_MODE", "professional")
    monkeypatch.setenv("KIMI_API_KEY", "sk-test-key")
    mode = get_mode()
    assert mode == "professional"


def test_get_mode_invalid_value(monkeypatch):
    """Test invalid mode defaults to educational"""
    monkeypatch.setenv("MEDEX_MODE", "invalid_mode")
    monkeypatch.setenv("KIMI_API_KEY", "sk-test-key")
    mode = get_mode()
    assert mode == "educational"


def test_get_config_structure(no_api_no_legacy):
    """Test config dictionary structure"""
    config = get_config()
    assert isinstance(config, dict)
    assert "api_key" in config
    assert "mode" in config
    assert "has_api" in config


def test_get_config_no_api(no_api_no_legacy):
    """Test config with no API key"""
    config = get_config()
    assert config["api_key"] == ""
    assert config["mode"] == "mock"
    assert config["has_api"] is False


def test_get_config_with_api(with_api_key, monkeypatch):
    """Test config with API key"""
    monkeypatch.setenv("MEDEX_MODE", "educational")
    config = get_config()
    assert config["api_key"] == "sk-test-dummy-key-for-testing-only"
    assert config["mode"] == "educational"
    assert config["has_api"] is True


def test_mode_case_insensitive(monkeypatch):
    """Test that mode is case insensitive"""
    monkeypatch.setenv("MEDEX_MODE", "EDUCATIONAL")
    monkeypatch.setenv("KIMI_API_KEY", "sk-test-key")
    mode = get_mode()
    assert mode == "educational"

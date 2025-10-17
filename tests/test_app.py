"""
Test application core functionality
"""

import pytest
from medex.app import run_once


def test_run_once_returns_string(no_api_no_legacy):
    """Test that run_once returns a string"""
    result = run_once("What is diabetes?")
    assert isinstance(result, str)
    assert len(result) > 0


def test_run_once_mock_mode(mock_mode):
    """Test run_once in mock mode"""
    query = "What is hypertension?"
    result = run_once(query)
    
    # Check for mock markers
    assert "MOCK RESPONSE" in result
    assert "mock" in result.lower()
    assert query in result


def test_run_once_respects_mode(no_api_no_legacy):
    """Test that run_once respects the mode setting"""
    result = run_once("Test query")
    assert "Mode: mock" in result


def test_run_once_explicit_mode(monkeypatch):
    """Test run_once with explicit mode parameter"""
    monkeypatch.delenv("KIMI_API_KEY", raising=False)
    result = run_once("Test query", mode="mock")
    assert "Mode: mock" in result


def test_run_once_educational_marker(mock_mode):
    """Test that response includes educational disclaimer"""
    result = run_once("Medical question")
    assert "EDUCATIONAL" in result.upper() or "educational" in result.lower()


def test_run_once_contains_query(mock_mode):
    """Test that response references the original query"""
    query = "What are the symptoms of diabetes?"
    result = run_once(query)
    assert query in result


def test_run_once_stable_format(mock_mode):
    """Test that mock responses have stable format for assertion"""
    result = run_once("Test query")
    
    # Check for stable markers
    assert "MOCK RESPONSE" in result
    assert "Mode:" in result
    assert "⚠️" in result or "WARNING" in result.upper()


def test_run_once_different_queries(mock_mode):
    """Test run_once with different queries"""
    queries = [
        "What is diabetes?",
        "Symptoms of hypertension",
        "Treatment for common cold",
    ]
    
    for query in queries:
        result = run_once(query)
        assert isinstance(result, str)
        assert len(result) > 0
        assert query in result


def test_run_once_empty_query(mock_mode):
    """Test run_once with empty query"""
    result = run_once("")
    assert isinstance(result, str)


def test_run_once_long_query(mock_mode):
    """Test run_once with long query"""
    query = "A patient presents with chest pain " * 20
    result = run_once(query)
    assert isinstance(result, str)
    assert len(result) > 0

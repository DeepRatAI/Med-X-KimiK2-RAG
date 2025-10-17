"""
Test adapters module
"""

import pytest
from medex.adapters import build_pipeline, answer_query


def test_build_pipeline_mock_mode(mock_mode):
    """Test that build_pipeline returns None in mock mode"""
    pipeline = build_pipeline(mode="mock")
    assert pipeline is None


def test_build_pipeline_default(no_api_no_legacy):
    """Test build_pipeline with default settings"""
    pipeline = build_pipeline()
    assert pipeline is None


def test_build_pipeline_educational_no_legacy(educational_mode):
    """Test build_pipeline in educational mode without legacy"""
    pipeline = build_pipeline(mode="educational")
    # Should return None since legacy not available
    assert pipeline is None


def test_answer_query_mock_response(mock_mode):
    """Test answer_query returns mock response"""
    result = answer_query(None, "What is diabetes?", mode="mock")
    
    assert isinstance(result, str)
    assert "MOCK RESPONSE" in result
    assert "Mode: mock" in result


def test_answer_query_contains_query(mock_mode):
    """Test that answer includes the query"""
    query = "What are symptoms of hypertension?"
    result = answer_query(None, query, mode="mock")
    
    assert query in result


def test_answer_query_educational_disclaimer(mock_mode):
    """Test that answer includes educational disclaimer"""
    result = answer_query(None, "Test query", mode="mock")
    
    assert "EDUCATIONAL" in result.upper() or "educational" in result.lower()


def test_answer_query_medical_disclaimer(mock_mode):
    """Test that answer includes medical disclaimer"""
    result = answer_query(None, "Test query", mode="mock")
    
    # Should mention not real medical advice
    assert any(
        phrase in result.lower()
        for phrase in ["not real", "educational", "consult", "professional"]
    )


def test_answer_query_stable_markers(mock_mode):
    """Test that mock responses have stable markers"""
    result = answer_query(None, "Test", mode="mock")
    
    # Check for stable markers for testing
    assert "MOCK RESPONSE" in result
    assert "Mode:" in result
    assert "⚠️" in result


def test_answer_query_different_modes():
    """Test answer_query with different modes"""
    query = "Test query"
    
    for mode in ["mock", "educational", "professional"]:
        result = answer_query(None, query, mode=mode)
        assert isinstance(result, str)
        assert f"Mode: {mode}" in result


def test_answer_query_none_pipeline(mock_mode):
    """Test answer_query with None pipeline"""
    result = answer_query(None, "Query", mode="mock")
    assert isinstance(result, str)
    assert "MOCK RESPONSE" in result


def test_answer_query_empty_query(mock_mode):
    """Test answer_query with empty query"""
    result = answer_query(None, "", mode="mock")
    assert isinstance(result, str)


def test_answer_query_special_characters(mock_mode):
    """Test answer_query with special characters"""
    query = "Test with special chars: áéíóú ñ ¿?"
    result = answer_query(None, query, mode="mock")
    assert isinstance(result, str)
    assert query in result

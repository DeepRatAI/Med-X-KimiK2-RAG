"""
Optional legacy integration tests
These tests are skipped by default and only run when legacy code is available
"""

import pytest
import sys


@pytest.mark.legacy
def test_medex_final_import():
    """Test importing MEDEX_FINAL if available"""
    try:
        import MEDEX_FINAL
        assert MEDEX_FINAL is not None
    except ImportError:
        pytest.skip("MEDEX_FINAL not available")


@pytest.mark.legacy
def test_medical_rag_system_import():
    """Test importing medical_rag_system if available"""
    try:
        import medical_rag_system
        assert medical_rag_system is not None
    except ImportError:
        pytest.skip("medical_rag_system not available")


@pytest.mark.legacy
def test_legacy_integration_smoke():
    """
    Smoke test for legacy integration
    Only runs if MEDEX_FINAL is available
    """
    try:
        import MEDEX_FINAL
        # Basic smoke test - just verify it doesn't crash
        assert hasattr(MEDEX_FINAL, "__file__")
    except ImportError:
        pytest.skip("MEDEX_FINAL not available")


@pytest.mark.legacy
def test_medex_does_not_require_legacy():
    """
    Test that medex package works without legacy
    This verifies the package can be used independently
    """
    # Remove legacy from sys.modules if present
    legacy_modules = [
        key for key in list(sys.modules.keys())
        if any(
            legacy in key
            for legacy in ["MEDEX_FINAL", "medical_rag_system", "MEDEX_ULTIMATE"]
        )
    ]
    for mod in legacy_modules:
        del sys.modules[mod]
    
    # Import and use medex
    from medex.app import run_once
    result = run_once("Test query", mode="mock")
    
    assert isinstance(result, str)
    assert "MOCK RESPONSE" in result
    
    # Verify legacy wasn't imported
    assert "MEDEX_FINAL" not in sys.modules

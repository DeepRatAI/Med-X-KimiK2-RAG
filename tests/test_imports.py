"""
Test basic imports and package structure
"""

import pytest


def test_import_medex():
    """Test that medex package can be imported"""
    import medex
    assert medex is not None


def test_medex_version():
    """Test that medex has a version attribute"""
    import medex
    assert hasattr(medex, "__version__")
    assert isinstance(medex.__version__, str)
    assert len(medex.__version__) > 0


def test_medex_version_format():
    """Test that version follows semantic versioning"""
    import medex
    parts = medex.__version__.split(".")
    assert len(parts) >= 2, "Version should have at least major.minor"


def test_import_config():
    """Test that config module can be imported"""
    from medex import config
    assert config is not None


def test_import_app():
    """Test that app module can be imported"""
    from medex import app
    assert app is not None


def test_import_adapters():
    """Test that adapters module can be imported"""
    from medex import adapters
    assert adapters is not None


def test_import_cli():
    """Test that cli module can be imported"""
    from medex import cli
    assert cli is not None


def test_public_api():
    """Test that public API functions are available"""
    import medex
    
    # Check public API
    assert hasattr(medex, "get_config")
    assert hasattr(medex, "get_mode")
    assert hasattr(medex, "run_once")


def test_no_legacy_imports_at_import_time():
    """Test that importing medex doesn't import legacy modules"""
    import sys
    
    # Remove legacy if present
    legacy_modules = [key for key in sys.modules if "MEDEX_FINAL" in key]
    for mod in legacy_modules:
        del sys.modules[mod]
    
    # Import medex
    import medex
    
    # Check that legacy wasn't imported
    assert "MEDEX_FINAL" not in sys.modules

# MedeX Testing Quick Start Guide

## Installation

```bash
# Install package with dev dependencies
pip install -e .[dev]
```

## Running Tests

### All Tests
```bash
pytest -q              # Quiet mode (default)
pytest -v              # Verbose mode
pytest                 # Standard output
```

### Specific Test Files
```bash
pytest tests/test_config.py -v
pytest tests/test_cli.py -v
pytest tests/test_app.py -v
```

### By Marker
```bash
pytest -m "not legacy"    # Skip legacy tests (default for CI)
pytest -m legacy          # Run only legacy tests (requires legacy code)
```

### With Coverage
```bash
pytest --cov=medex --cov-report=html
# Open htmlcov/index.html to view report
```

## Test Results Summary

**Total**: 62 tests
- **Passing**: 59 ✅
- **Skipped**: 3 (legacy tests)
- **Failed**: 0

### Test Breakdown
- `test_imports.py`: 9 tests - Package structure
- `test_config.py`: 12 tests - Configuration management
- `test_app.py`: 10 tests - Application core
- `test_adapters.py`: 12 tests - RAG adapters
- `test_cli.py`: 15 tests - CLI interface
- `test_legacy_opt.py`: 4 tests - Legacy integration (3 skipped)

## Using the CLI

### Check Version
```bash
medex --version
```

### Query (Mock Mode)
```bash
medex query --query "What is diabetes?"
medex query -q "Test query" --mode mock
```

### Show Configuration
```bash
medex config
```

### Show Info
```bash
medex info
```

## Python API Usage

```python
import medex

# Check version
print(medex.__version__)

# Get current mode
mode = medex.get_mode()
print(f"Mode: {mode}")

# Get configuration
config = medex.get_config()
print(config)

# Process a query
response = medex.run_once("What is diabetes?", mode="mock")
print(response)
```

## Environment Variables

- `KIMI_API_KEY`: API key (optional, defaults to mock mode)
- `MEDEX_MODE`: Operation mode (`mock`, `educational`, `professional`)

## Mock Mode

When no API key is set, the system automatically uses mock mode:

```bash
# No API key needed
unset KIMI_API_KEY
medex query -q "Test"
# Returns mock response
```

Mock responses include:
- `"MOCK RESPONSE"` marker
- `"Mode: mock"` indicator
- Original query
- Educational disclaimer

## Test Fixtures

Available in `tests/conftest.py`:

- `no_api_no_legacy`: Forces mock mode, removes legacy
- `mock_mode`: Sets mock mode explicitly
- `educational_mode`: Sets educational mode
- `with_api_key`: Sets dummy API key

Example usage:
```python
def test_example(mock_mode):
    """Test with mock mode fixture"""
    from medex import run_once
    result = run_once("Test")
    assert "MOCK RESPONSE" in result
```

## Common Issues

### Import Errors
**Problem**: `ModuleNotFoundError: No module named 'medex'`  
**Solution**: Install package: `pip install -e .[dev]`

### CLI Not Found
**Problem**: `medex: command not found`  
**Solution**: Reinstall package: `pip install -e .[dev]`

### Tests Fail with API Errors
**Problem**: Tests require API key  
**Solution**: Use fixtures (`no_api_no_legacy`, `mock_mode`)

### Legacy Tests Fail
**Problem**: Legacy modules not available  
**Solution**: Tests should skip automatically. If not, run: `pytest -m "not legacy"`

## CI/CD Integration

Tests run automatically in GitHub Actions without:
- API keys
- Network access
- GPU
- Legacy code

Example workflow step:
```yaml
- name: Run tests
  run: |
    pip install -e .[dev]
    pytest -q
```

## Documentation

- `TEST_PLAN.md`: Comprehensive test strategy
- `DELIVERY_SUMMARY.md`: Detailed implementation summary
- `README.md`: Project overview

## Support

For issues or questions:
1. Check test output for specific errors
2. Review `TEST_PLAN.md` for strategy details
3. Open an issue on GitHub
4. Contact: info@deeprat.tech

---

**Quick Health Check**:
```bash
# Run this to verify everything works
pytest -q && medex --version && medex query -q "Test"
```

If all three succeed, your setup is complete! ✅

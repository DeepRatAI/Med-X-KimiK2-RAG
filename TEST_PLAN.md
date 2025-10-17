# MedeX Test Plan

## Overview

This document describes the test suite for the MedeX package (`medex/`). The test suite is designed to work in CI environments without requiring API keys, network access, GPU, or legacy code dependencies.

## Test Architecture

### Test Discovery
- Tests are located in the `tests/` directory
- Configured via `pytest.ini` with:
  - Test path: `tests/`
  - Pattern: `test_*.py`
  - Quiet mode by default (`-q`)

### Test Markers
- `@pytest.mark.legacy`: Tests that require legacy code (`MEDEX_FINAL`, etc.)
  - Skipped by default in CI
  - Only run when legacy modules are available locally

## Test Modules

### 1. `test_imports.py` - Package Structure Tests
**Purpose**: Verify package structure and imports

**Tests**:
- Package can be imported successfully
- Version attribute exists and follows semantic versioning
- Core modules (config, app, adapters, cli) can be imported
- Public API is available (`get_config`, `get_mode`, `run_once`)
- No legacy imports happen at import time

**Coverage**: Package integrity, API surface

### 2. `test_config.py` - Configuration Tests
**Purpose**: Verify configuration management and environment variables

**Tests**:
- API key retrieval (with/without key)
- Mode detection (mock, educational, professional)
- Mode defaults to mock when no API key
- Invalid mode handling
- Config dictionary structure
- Case-insensitive mode handling

**Coverage**: Environment configuration, mode logic

### 3. `test_app.py` - Application Core Tests
**Purpose**: Test main application entry point `run_once()`

**Tests**:
- Returns string in mock mode
- Response contains mock markers
- Respects mode settings
- Includes educational disclaimers
- Contains original query in response
- Handles empty and long queries
- Stable format for assertions

**Coverage**: Core application logic, mock behavior

### 4. `test_adapters.py` - Adapter Layer Tests
**Purpose**: Test RAG pipeline and query processing adapters

**Tests**:
- `build_pipeline()` returns None in mock mode
- `answer_query()` returns mock response with stable markers
- Response includes query, mode, disclaimers
- Handles different modes (mock, educational, professional)
- Handles special characters and empty queries
- No network calls in mock mode

**Coverage**: Adapter layer, RAG integration points

### 5. `test_cli.py` - CLI Interface Tests
**Purpose**: Test command-line interface using Click's CliRunner

**Tests**:
- Version command works
- Help command displays usage
- Query command with various options
- Mode parameter handling
- Config command shows settings
- Info command displays version
- Error handling (missing parameters, invalid modes)
- Special character handling

**Coverage**: CLI functionality, user interface

### 6. `test_legacy_opt.py` - Optional Legacy Tests
**Purpose**: Test integration with legacy code when available

**Tests** (all marked with `@pytest.mark.legacy`):
- Legacy module imports (MEDEX_FINAL, medical_rag_system)
- Basic smoke tests for legacy integration
- Verify medex works independently of legacy

**Coverage**: Legacy compatibility (optional)

## Test Fixtures (conftest.py)

### `no_api_no_legacy`
Forces mock mode by:
- Clearing `KIMI_API_KEY` environment variable
- Setting `MEDEX_MODE=mock`
- Removing legacy modules from `sys.modules`

### `mock_mode`
Explicitly sets mock mode:
- `MEDEX_MODE=mock`
- Clears API key

### `educational_mode`
Sets educational mode:
- `MEDEX_MODE=educational`
- Clears API key (forces mock due to no key)

### `with_api_key`
Sets a dummy API key for testing:
- `KIMI_API_KEY=sk-test-dummy-key-for-testing-only`

## Mock Mode Strategy

The test suite relies on **mock mode** for CI compatibility:

1. **No Network**: Mock responses are generated locally
2. **No API Keys**: Works without KIMI_API_KEY
3. **No Legacy**: Doesn't require MEDEX_FINAL or other legacy modules
4. **Deterministic**: Responses have stable markers for assertions

### Mock Response Format
```
MOCK RESPONSE for query: "<query>"

Mode: <mode>

This is a simulated response...

⚠️ EDUCATIONAL USE ONLY
```

### Stable Markers for Testing
- `"MOCK RESPONSE"`: Identifies mock output
- `"Mode: <mode>"`: Shows current mode
- `"⚠️"`: Educational disclaimer marker
- Query text appears in response

## Running Tests

### Locally
```bash
# Run all tests
pytest -q

# Verbose output
pytest -v

# Run specific test file
pytest tests/test_config.py -v

# Run with coverage
pytest --cov=medex --cov-report=html
```

### In CI (GitHub Actions)
```bash
# Install dependencies
pip install -e .[dev]

# Run tests
pytest -q
```

**CI Environment**:
- No `KIMI_API_KEY` set
- No legacy code available
- Linux, CPU only
- No network access to external services

### Running Legacy Tests Locally
```bash
# Run only legacy tests (requires legacy code)
pytest -v -m legacy

# Skip legacy tests (default)
pytest -v -m "not legacy"
```

## Test Coverage Goals

- **Package imports**: 100%
- **Configuration**: 100%
- **Mock mode**: 100%
- **CLI interface**: >90%
- **Adapters**: >90%
- **Legacy integration**: Optional, not counted in CI

## Success Criteria

✅ All tests pass in CI without:
- API keys
- Network access
- GPU
- Legacy code dependencies

✅ CLI works in mock mode
✅ Tests are deterministic and stable
✅ No import-time dependencies on legacy modules
✅ Mock responses have stable, assertable markers

## Error Scenarios Tested

1. **Missing API key**: Falls back to mock mode
2. **Invalid mode**: Defaults to educational
3. **Missing CLI parameters**: Shows error message
4. **Empty queries**: Handled gracefully
5. **Special characters**: Properly encoded/decoded
6. **Legacy unavailable**: Tests skip gracefully

## Future Enhancements

- Add integration tests with RAG stubs (no network)
- Add error coverage tests (network failures, etc.)
- Add performance benchmarks for mock mode
- Add tests for event loop handling
- Add tests for concurrent queries

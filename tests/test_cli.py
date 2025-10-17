"""
Test CLI functionality
"""

import pytest
from click.testing import CliRunner
from medex.cli import cli


@pytest.fixture
def runner():
    """Create a CLI runner for testing"""
    return CliRunner()


def test_cli_version(runner):
    """Test CLI version command"""
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "medex" in result.output.lower()


def test_cli_help(runner):
    """Test CLI help command"""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "MedeX" in result.output


def test_cli_query_basic(runner, mock_mode):
    """Test basic query command"""
    result = runner.invoke(cli, ["query", "--query", "What is diabetes?"])
    assert result.exit_code == 0
    assert "MOCK RESPONSE" in result.output


def test_cli_query_short_option(runner, mock_mode):
    """Test query with short option -q"""
    result = runner.invoke(cli, ["query", "-q", "Test query"])
    assert result.exit_code == 0
    assert "MOCK RESPONSE" in result.output


def test_cli_query_with_mode(runner, no_api_no_legacy):
    """Test query with explicit mode"""
    result = runner.invoke(
        cli, ["query", "--mode", "mock", "--query", "Test query"]
    )
    assert result.exit_code == 0
    assert "MOCK RESPONSE" in result.output
    assert "Mode: mock" in result.output


def test_cli_query_educational_mode(runner, no_api_no_legacy):
    """Test query in educational mode"""
    result = runner.invoke(
        cli, ["query", "--mode", "educational", "-q", "Test"]
    )
    assert result.exit_code == 0


def test_cli_query_without_query(runner):
    """Test query command without query parameter"""
    result = runner.invoke(cli, ["query"])
    assert result.exit_code != 0  # Should fail without required option


def test_cli_config_command(runner, mock_mode):
    """Test config command"""
    result = runner.invoke(cli, ["config"])
    assert result.exit_code == 0
    assert "Mode:" in result.output
    assert "API Key configured:" in result.output


def test_cli_config_shows_mock(runner, no_api_no_legacy):
    """Test config shows mock mode"""
    result = runner.invoke(cli, ["config"])
    assert result.exit_code == 0
    assert "mock" in result.output.lower()


def test_cli_info_command(runner, mock_mode):
    """Test info command"""
    result = runner.invoke(cli, ["info"])
    assert result.exit_code == 0
    assert "MedeX" in result.output
    assert "mode:" in result.output.lower()


def test_cli_query_output_contains_query(runner, mock_mode):
    """Test that CLI output contains the original query"""
    query = "What is hypertension?"
    result = runner.invoke(cli, ["query", "-q", query])
    assert result.exit_code == 0
    assert query in result.output


def test_cli_query_educational_disclaimer(runner, mock_mode):
    """Test that CLI output includes educational disclaimer"""
    result = runner.invoke(cli, ["query", "-q", "Test"])
    assert result.exit_code == 0
    assert (
        "EDUCATIONAL" in result.output.upper() or "educational" in result.output
    )


def test_cli_multiple_queries(runner, mock_mode):
    """Test multiple sequential queries"""
    queries = ["Query 1", "Query 2", "Query 3"]
    
    for query in queries:
        result = runner.invoke(cli, ["query", "-q", query])
        assert result.exit_code == 0
        assert query in result.output


def test_cli_query_with_special_chars(runner, mock_mode):
    """Test query with special characters"""
    query = "¿Qué es la diabetes?"
    result = runner.invoke(cli, ["query", "-q", query])
    assert result.exit_code == 0


def test_cli_invalid_mode(runner):
    """Test query with invalid mode"""
    result = runner.invoke(
        cli, ["query", "--mode", "invalid", "-q", "Test"]
    )
    # Should fail due to invalid choice
    assert result.exit_code != 0

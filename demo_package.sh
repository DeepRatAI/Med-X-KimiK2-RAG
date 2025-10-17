#!/bin/bash
# MedeX Package Demo Script
# Demonstrates the packaging capabilities without requiring actual installation

set -e

echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║          🏥 MedeX v0.1.0 - Package Installation Demo                    ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Must run from repository root directory"
    exit 1
fi

echo "📋 Step 1: Verify package structure"
echo "------------------------------------------------------------"
python3 -c "import medex; print(f'✅ Package version: {medex.__version__}')" 2>/dev/null && \
echo "✅ MedeX package is importable" || \
echo "⚠️  Package not yet installed (run pip install -e .)"

echo ""
echo "📋 Step 2: Test CLI functionality (mock mode)"
echo "------------------------------------------------------------"
export PYTHONPATH="${PWD}"
python3 -m medex.cli --mode educational --query "¿Qué es la diabetes?" | head -20

echo ""
echo "📋 Step 3: Run tests"
echo "------------------------------------------------------------"
pytest -q tests/test_smoke.py 2>/dev/null || echo "⚠️  pytest not available or tests failed"

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║                          ✅ Demo Complete!                               ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""
echo "📚 Quick Reference:"
echo ""
echo "   Installation:"
echo "   $ pip install -e ."
echo ""
echo "   CLI Usage:"
echo "   $ medex --mode educational --query \"¿Qué es la diabetes?\""
echo "   $ medex --mode professional --query \"Paciente con dolor torácico\""
echo ""
echo "   Python API:"
echo "   >>> from medex.app import run_once"
echo "   >>> response = run_once(\"¿Qué es la diabetes?\", mode=\"educational\")"
echo ""
echo "   Streamlit (legacy app still works):"
echo "   $ streamlit run streamlit_app.py"
echo ""
echo "   Testing:"
echo "   $ pytest -q tests/test_smoke.py"
echo ""
echo "⚠️  Note: For full functionality, set KIMI_API_KEY environment variable"
echo "   or create api_key.txt with your Moonshot API key"
echo ""

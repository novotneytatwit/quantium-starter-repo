#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run the test suite
python3 -m pytest tests/
TEST_EXIT_CODE=$?

# Exit with 0 if tests passed, 1 if any failed
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed."
    exit 0
else
    echo "❌ Some tests failed."
    exit 1
fi
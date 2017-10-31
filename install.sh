#!/bin/bash
export ERROR_COUNT=50
export CONVENTION_COUNT=100
export WARNINGS=100
export CODEBASE="/home/kuliza-356/zwork/stock-market/stock-market"
export THRESHOLD_LINT_SCORE=9.0 # fix hack later

python pylint-hook.py
echo "Patched!"
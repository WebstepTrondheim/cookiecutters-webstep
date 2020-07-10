#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
echo "======== pylint ========"
poetry run python -m pylint {{cookiecutter.project_slug}}
exit_pylint=$?
echo ""
echo "======== black ========"
poetry run python -m black --check --diff {{cookiecutter.project_slug}}
exit_black=$?
echo ""
echo "======== isort ========"
poetry run python -m isort --check-only --diff
exit_isort=$?
echo ""
echo "======== mypy ========"
poetry run python -m mypy --ignore-missing-imports --strict {{cookiecutter.project_slug}}
exit_mypy=$?
echo ""
echo "======== pydocstyle ========"
poetry run python -m pydocstyle --convention=numpy --add-ignore=D105 {{cookiecutter.project_slug}}
exit_pydocstyle=$?
echo ""
echo "======== pytest ========"
poetry run python -m pytest --junit-xml=test-reports/pytest.xml --cov={{cookiecutter.project_slug}} --cov-report=xml:test-reports/coverage.xml --cov-report=html:test-reports/coverage
exit_pytest=$?
echo ""
echo ""
echo "======== exit stati ========"
echo "pylint: $exit_pylint, black: $exit_black, isort: $exit_isort, mypy: $exit_mypy, pydocstyle: $exit_pydocstyle, pytest: $exit_pytest"
! (( $exit_pylint || $exit_black || $exit_isort || $exit_mypy || $exit_pydocstyle || $exit_pytest ))
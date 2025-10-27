
# Makefile: lint target runs a pre-format step with black over project Python files.
# Behavior:
# - If a virtualenv exists at ./venv/Scripts/python.exe it will use that Python to run
#   `python -m black` (so black must be installed in the venv).
# - Otherwise it falls back to `python -m black` (system python).
# - Files are discovered first via `git ls-files '*.py'` (safe for excluding venv),
#   falling back to `find` and excluding typical venv dirs.

VENV_DIR := venv
# Detect both POSIX and Windows venv python locations
VENV_PY_WIN := $(VENV_DIR)/Scripts/python.exe
VENV_PY_POSIX := $(VENV_DIR)/bin/python

# Determine which Python to use (POSIX, Windows, or system)
PYTHON := $(if $(wildcard $(VENV_PY_POSIX)),$(VENV_PY_POSIX),\
		$(if $(wildcard $(VENV_PY_WIN)),$(VENV_PY_WIN),python))

# If DRY_RUN is set (non-empty), the Make targets will print the commands instead of executing them.
DRY_RUN_FLAG := $(if $(strip $(DRY_RUN)),-DryRun,)

# Collect python files: prefer git-tracked files; fallback to find (exclude venv)
PYFILES := $(shell git ls-files '*.py' 2>/dev/null || \
	find . -name '*.py' -not -path './$(VENV_DIR)/*' -not -path './.venv/*' 2>/dev/null | sed 's|^./||')

.PHONY: lint
lint:
	@echo "Preformateando archivos Python con black..."
	@echo "Archivos detectados: $(PYFILES)"
	@echo "Usando $(PYTHON)"
	@if [ -n "$(DRY_RUN)" ]; then \
		echo "DRY RUN: $(PYTHON) -m black $(PYFILES)"; \
	else \
		$(PYTHON) -m black $(PYFILES); \
	fi

.PHONY: lint-pwsh
lint-pwsh:
	@echo "Formateando usando PowerShell (Windows). Si quieres probar sin ejecutar, usa -DryRun en el script."
	@pwsh -NoProfile -ExecutionPolicy Bypass -File ./scripts/format.ps1 $(DRY_RUN_FLAG)

.PHONY: test tests-pwsh tests

# Detect OS for choosing the right test command
ifeq ($(OS),Windows_NT)
    # On Windows, default to PowerShell script
    tests: tests-pwsh
else
    # On POSIX systems (Linux, macOS), use standard tests target
    tests: tests
endif

# PowerShell target for Windows
tests-pwsh:
	@pwsh -NoProfile -ExecutionPolicy Bypass -File ./scripts/run_tests.ps1 $(DRY_RUN_FLAG)

# Standard test target (works on all systems, preferred on POSIX)
tests:
	@echo "Ejecutando tests con pytest..."
	@echo "Usando $(PYTHON)"
	@if [ -n "$(DRY_RUN)" ]; then \
		echo "DRY RUN: $(PYTHON) -m pytest -v"; \
	else \
		$(PYTHON) -m pytest -v; \
	fi


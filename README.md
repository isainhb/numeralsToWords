# Numerals To Words

````markdown
# Numerals To Words

## Requirements
- Python 3.8+ (works on 3.8 through 3.13 tested)

## Prerequisites
1. Create a virtual environment:
# Numerals To Words

Simple utility to convert numerals (hours and minutes) to words.

## Requirements

- Python 3.8 or newer (tested up to 3.13).

## Prerequisites

1. Create a virtual environment:

```sh
python -m venv venv
```

2. Activate the virtual environment:

- On Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

- On Windows (cmd.exe):

```cmd
.\venv\Scripts\activate.bat
```

- On macOS / Linux:

```sh
source venv/bin/activate
```

3. Install project dependencies:

```sh
pip install -r requirements.txt
```

4. Optional: If you are using Windows and don't have Make installed, you can install it via Chocolatey:
```sh
choco install make --version=3.81
```

## Run

From the project root, run:

```sh
python app.py
```

Pass the required input (hour and minute) as described in the application usage.

## Tests

The project includes Make targets to run tests using pytest in verbose mode, with automatic virtualenv detection.

Standard test command (recommended, works everywhere):
```sh
make tests
```

System-specific alternatives:
- Windows (PowerShell):
```powershell
make tests-pwsh
```
- Any system (alias that picks the right command):
```sh
make tests
```

Dry-run options (show command without executing):
```sh
make tests DRY_RUN=1      # Standard
make tests-pwsh DRY_RUN=1  # Windows PowerShell
```

The tests commands will:
1. Use Python from `venv/bin/python` if it exists (POSIX)
2. Or try `venv/Scripts/python.exe` (Windows)
3. Fall back to system Python if no virtualenv is found

Alternative direct commands:
```sh
# Run all tests with pytest
pytest -v

# Run a specific test file
python -m unittest tests/utest_time_to_words.py
```

Note: The `make tests` target is the standard way to run tests and works on all platforms. Use `make tests-pwsh` if you specifically need PowerShell handling on Windows.

## Formatting / Linting (black)

This repository includes both a `Makefile` target and a PowerShell helper to run `black` over project files.

POSIX (macOS / Linux)

- Use `make lint` from the repository root. The `Makefile` will:
  1. Prefer `venv/bin/python -m black` when a POSIX venv exists.
  2. Otherwise try `venv/Scripts/python.exe -m black` (Windows-style venv path) if present.
  3. Fall back to `python -m black` (system) if no venv is found.

Example:

```sh
make lint
```

Dry-run (print the command without executing):

```sh
make lint DRY_RUN=1
```

Windows (PowerShell)

- Use the included PowerShell script `scripts/format.ps1`, which performs file discovery and venv detection.

Dry-run (only prints the command):

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\format.ps1 -DryRun
```

Run for real:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\format.ps1
```

If `make` is available on Windows (Git Bash, WSL, Chocolatey), you can also run:

```powershell
make lint-pwsh
```

Notes

- The `Makefile` prefers `git ls-files '*.py'` to discover project Python files (avoids formatting files inside `venv`). If `git` is not available it falls back to a recursive search that excludes typical venv paths.
- Ensure `black` is installed in the active virtual environment or globally. The commands call `python -m black`.

If you'd like the `Makefile` to behave differently (for example a separate `format` target or a `DRY_RUN` default), tell me and I will add it.


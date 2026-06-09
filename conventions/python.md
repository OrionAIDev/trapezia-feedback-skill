# Python conventions

Applies to any skill that ships Python code (T1/T2).

## Documentation

- **Google-style docstrings** on every module, class, method, and function.
  Non-negotiable; the `docstrings.present` validator check will WARN if any are missing.
- Module docstrings: 1-3 sentences explaining the module's purpose.
- Function/method docstrings: include `Args:`, `Returns:`, and `Raises:` sections.
  Put type information in type hints, not in docstrings.

## CLI surface

- Use `argparse` (stdlib). Use `click` only if explicitly opted in.
- Every CLI must support `--help`.
- Subcommand naming: verb-noun (`add-entry`, `list-records`).

## Style and packaging

- PEP 8.
- Type hints on all public functions (`def foo(x: int) -> str:`).
- Prefer stdlib + well-supported third-party libraries.
- `pyproject.toml` over `setup.py` for new Python packages.
- `src/` layout for installable packages.

## Anti-patterns (the `trapezia-skill-audit` auditor flags these)

- LLM-generated logic in irreversible / safety-critical paths (money, credentials,
  deletion, external sends, auth checks). Code only — no LLM judgment.
- Bare `except:`.
- Mutating default arguments.
- Print-debugging left in committed code.
- Secrets or `.env` values committed to the repo.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A small MCP server (`FastMCP("docs")`) that exposes document-processing tools to AI assistants. It is a self-contained uv project nested inside the larger `claude_api_tutorial` repo: it has its own `pyproject.toml`, `uv.lock` and `.venv`, separate from the parent repo's. Run all commands from this directory (`notebooks/app_starter`) so uv picks up this project, not the parent.

## Commands

```bash
uv venv && uv pip install -e .          # setup (activate .venv first if installing manually)
uv run main.py                          # start the MCP server (stdio)
uv run mcp dev main.py                  # MCP Inspector for poking at tools interactively (mcp[cli])
uv run pytest                           # all tests
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_pdf   # single test
```

No linter or formatter is configured.

## Architecture

- `tools/` holds plain Python functions, one module per domain (`math.py`, `document.py`). They have no MCP dependency and are unit-testable directly.
- `main.py` is the only place tools become MCP tools, via `mcp.tool()(fn)`. A function in `tools/` is not exposed until it is registered here. Currently only `add` is registered; `binary_document_to_markdown` is implemented and tested but not yet registered.
- `tools/document.py` wraps `markitdown` and converts in-memory bytes (`BytesIO` + `StreamInfo(extension=...)`), not file paths. Supported formats come from the `markitdown[docx,pdf]` extras.
- Tests import `tools.*` as a top-level package, so pytest has to run from the project root. Binary fixtures live in `tests/fixtures/` (`mcp_docs.docx`, `mcp_docs.pdf`).

## Naming

- Always use descriptive variable names that clearly indicate what the variable holds (e.g. `cashBalance`, not `cb`).
- Use camelCase for variables, starting with a lowercase letter.

## Tool definition conventions

FastMCP builds the tool schema from the function signature and docstring, so both are part of the tool's contract with the model:

- Describe every parameter with `pydantic.Field(description=...)` as its default value (see `tools/math.py`).
- Docstrings: a one-line summary, then a detailed explanation, when to use (and not use) the tool, and examples with expected input/output.

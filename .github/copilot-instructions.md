# Copilot Workspace Instructions

## Mandatory Development Checklist

**REQUIRED** before any commit or PR:

- [ ] `uv run ruff check .` (lint)
- [ ] `uv sync` (build/install dependencies)
- [ ] `uv run pytest` (test)

## Project Overview

Soc Ops: Social Bingo game (FastAPI + Jinja2 + HTMX). Players match questions to mark squares and get 5 in a row.

## Architecture

```
app/
├── templates/       # Jinja2 HTML (base.html, home.html, components/)
├── static/          # CSS/JS assets
├── models.py        # Pydantic models (GameState, BingoSquare)
├── game_logic.py    # Board generation & bingo detection
├── game_service.py  # Session management (GameSession)
├── data.py          # Question bank
└── main.py          # FastAPI routes & HTMX endpoints
tests/               # API & game logic tests
```

## Key Commands

```bash
uv sync                                    # Install deps
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000  # Dev server
uv run pytest                              # Tests
uv run ruff check .                        # Lint
```

## Styling & Design

- Custom CSS utilities in `app/static/css/app.css` (Tailwind-like)
- Frontend: Follow [.github/instructions/frontend-design.instructions.md](.github/instructions/frontend-design.instructions.md) for creative designs
- CSS utils: See [.github/instructions/css-utilities.instructions.md](.github/instructions/css-utilities.instructions.md)

## Design Guide

- Use strong, cohesive themes rather than generic layouts. Commit to a distinctive visual direction like Gotham noir, neon cyber-core, or modern glass.
- Prefer bold typography, atmospheric backgrounds, and subtle motion over plain white page defaults.
- Keep layout responsive and preserve existing HTMX targets/IDs when changing components.
- Add new utility classes in `app/static/css/app.css` only when needed instead of duplicating inline styles.
- Preserve functionality first: visual updates should not change route or template logic.

## State & Rules

- Server-side state via `GameSession` (cookie-persisted)
- HTMX for partial updates
- **Do NOT use VS Code Simple Browser** - HTMX needs full browser</content>
<parameter name="filePath">/workspaces/my-soc-ops-python/.github/copilot-instructions.md
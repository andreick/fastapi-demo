#!/usr/bin/env bash
poetry config virtualenvs.in-project true
poetry install --no-root
poetry run alembic upgrade head

#!/bin/sh

cd app
#alembic upgrade head || exit 1
uvicorn main:app --host 0.0.0.0

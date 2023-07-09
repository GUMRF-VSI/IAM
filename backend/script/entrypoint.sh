#!/bin/sh

cd app
aerich upgrade || exit 1
uvicorn main:app --host 0.0.0.0

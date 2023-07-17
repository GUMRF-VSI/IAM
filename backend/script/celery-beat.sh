#!/bin/sh

cd app

celery -A core.scheduler beat --loglevel=info

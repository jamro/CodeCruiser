#!/bin/sh

cd "$(dirname "$0")/../backend"
python3 -m uvicorn main:app --host 0.0.0.0 --port 80
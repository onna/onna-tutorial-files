#!/bin/sh
set -a
echo "Processing config ...";
envsubst '$ONNA_USER,$ONNA_ACCOUNT,$ONNA_CONTAINER'< auth.py > run-auth.py
python run-auth.py
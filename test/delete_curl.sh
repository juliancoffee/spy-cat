#!/usr/bin/env bash

#set -xeuo pipefail # to print all executed the commands
set -euo pipefail

if [ -z "${1:-}" ]
then
    echo "provide cat id as first argument, error"
    exit
fi

# -w to add newline at the end
curl \
    --request DELETE \
    -w "\n" \
    "http://localhost:8000/cat/$1/"

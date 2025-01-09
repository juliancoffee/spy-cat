#!/usr/bin/env bash

#set -xeuo pipefail # to print all the commands
set -euo pipefail

if [ -z "${1:-}" ]
then
    echo "provide cat id as first argument, error"
    exit
fi

if [ -z "${2:-}" ]
then
    echo "provide cat salary as second argument, error"
    exit
fi

curl \
    --header "Content-Type: application/json" \
    -X PATCH \
    --data "{\"salary\": $2}" \
    "http://localhost:8000/cat/$1/"

echo "" # add newline just in case

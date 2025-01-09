#!/usr/bin/env bash

#set -xeuo pipefail # to print all the commands
set -euo pipefail

if [ -z "${1:-}" ]
then
    echo "provide target id as first argument, error"
    exit
fi

if [ -z "${2:-}" ]
then
    echo "provide notes as second argument, error"
    exit
fi

curl \
    --header "Content-Type: application/json" \
    -X PATCH \
    --data "{\"notes\": \"$2\"}" \
    "http://localhost:8000/target/$1/"

echo "" # add newline just in case

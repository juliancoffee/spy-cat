#!/usr/bin/env bash

#set -xeuo pipefail # to print all the commands
set -euo pipefail

curl \
    --header "Content-Type: application/json" \
    -X POST \
    --data "@sample/bad_cat.json" \
    http://localhost:8000/cat/create/

echo "" # add newline just in case

#!/usr/bin/env bash

#set -xeuo pipefail # to print all executed the commands
set -euo pipefail

# while I'm writing all of this, I'm surprised that
# there's no automatic tool for vanilla Django to generate
# interactive API docs
#
# another point to Django Rest Framework, I guess

# -w to add newline at the end
curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data "@sample/mission.json" \
    -w "\n" \
    http://localhost:8000/mission/create/

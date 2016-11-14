#!/bin/sh

if [ -f /secret/env ]; then
    set -a
    . /secret/env
else
    mkdir -p /secret
    env > /secret/env
fi

exec "$@"
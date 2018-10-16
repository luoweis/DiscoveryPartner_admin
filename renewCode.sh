#!/bin/bash
echo "renew code..."
sleep 10
git fetch --all
git reset --hard origin/dev
git pull
echo "renew end!"
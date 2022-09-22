#!/usr/bin/env bash

curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2

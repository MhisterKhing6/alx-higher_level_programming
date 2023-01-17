#!/bin/bash
# display all HTTP methods the server will accept using curl
curl -sI "$1" | awk -F ": " '/Allow/ {print $2}'
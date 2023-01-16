#!/bin/bash
# Create get the size of a page
curl -w '%{size_download}' -s -o /dev/null  "$1"


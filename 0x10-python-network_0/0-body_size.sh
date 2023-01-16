#!/usr/bin/env bash
# Create get the size of a page

if(("$#" != 0))
then curl -w '%{size_download}' -s -o /dev/null "$1"
fi

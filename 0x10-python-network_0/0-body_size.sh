#!/bin/bash
# Create get the size of a page
if(("$#" != 0))
then 
  t_size=$(curl -w '%{size_download}' -s -o /dev/null  "$1")
  h_size=$(curl -w '%{size_header}' -s -o /dev/null "$1")
  echo "$((t_size - h_size))"
fi

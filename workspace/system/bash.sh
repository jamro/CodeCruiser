#!/bin/bash

# Check if there are arguments passed
if [ "$#" -eq 0 ]; then
  echo "No arguments provided."
  exit 1
fi

# Pass all arguments to a new bash instance
bash -c "$*"
#!/bin/bash

# Navigate to the "media" folder
cd media

# Find and remove all .mp4 and .svg files in the current directory and its subdirectories
find . -type f \( -name "*.mp4" -o -name "*.svg" \) -exec rm -f {} +

# Return to the original directory
cd -

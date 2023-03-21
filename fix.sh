#!/bin/bash

# Split the PATH variable into an array using ":" as the delimiter
IFS=: read -ra PATH_ARRAY <<< "$PATH"

# Use awk to remove duplicates from the array and store the results in a new array
NEW_PATH_ARRAY=($(echo "${PATH_ARRAY[@]}" | awk -v RS=: '!a[$0]++'))

# Join the new array into a single string using ":" as the delimiter
NEW_PATH=$(IFS=:; echo "${NEW_PATH_ARRAY[*]}")

# Export the new PATH variable
export PATH="$NEW_PATH"

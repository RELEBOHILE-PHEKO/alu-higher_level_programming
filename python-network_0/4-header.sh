#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request with curl and display the body of the response
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"

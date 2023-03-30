#!/bin/bash
# URL, sends a GET request to URL, and displays the response body
curl -s "$1" -X GET -L

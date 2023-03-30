#!/usr/bin/bash
# script that takes in a URL, sends a request to it , 
# and displays the size of the body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'

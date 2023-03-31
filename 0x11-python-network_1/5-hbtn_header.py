#!/usr/bin/python3
"""
A script that takes in a URL, requests it & displays 
variable X-Request-Id value in the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))

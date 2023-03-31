#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to it 
and displays the value of the X-Request-Id variable
Use the packages urllib and sys, and with only.
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))

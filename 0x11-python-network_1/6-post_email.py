#!/usr/bin/python3
"""
A script that takes in a URL and an email address,
POSTs a request to it with the email parameter,
then displays the body of the response.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)

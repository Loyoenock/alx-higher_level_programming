# 0x11. Python - Network #1

## Resources
__Read or watch:__

	* [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
	* [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
	* [Requests package](https://pypi.org/project/requests/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
	* How to fetch internet resources with the Python package urllib
	* How to decode urllib body response
	* How to use the Python package requests #requestsiswaysimplerthanurllib
	* How to make HTTP GET request
	* How to make HTTP POST/PUT/etc. request
	* How to fetch JSON resources
	* How to manipulate data from an external service

## Requirements
### General

	* Allowed editors: vi, vim, emacs
	* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	* All your files should end with a new line
	* The first line of all your files should be exactly #!/usr/bin/python3
	* A README.md file at the root of the repo, containing a description of the repository	
	* A README.md file, at the root of the folder of this project, is mandatory	
	* Your code should use the pycodestyle (version 2.8.*)
	* All your files must be executable
	* The length of your files will be tested using wc
	* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	* You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
	* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
	* Your code should not be executed when imported (by using if __name__ == "__main__":)

### Tasks

[0. What's my status? #0](./0-hbtn_status.py)

Write a Python script that fetches https://alx-intranet.hbtn.io/status

	* You must use the package urllib
	* You are not allowed to import any packages other than urllib
	* The body of the response must be displayed like the following example (tabulation before -)
	* You must use a with statement

```
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
```

[1. Response header value #0](./1-hbtn_header.py)

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

	* You must use the packages urllib and sys
	* You are not allow to import packages other than urllib and sys
	* The value of this variable is different for each request
	* You don’t need to check arguments passed to the script (number or type)
	* You must use a with statement

```
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 

```

[2. POST an email #0](./2-post_email.py)
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

	* The email must be sent in the email variable
	* You must use the packages urllib and sys
	* You are not allowed to import packages other than urllib and sys
	* You don’t need to check arguments passed to the script (number or type)
	* You must use the with statement
	* Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 

```

[3. Error code #0](./3-error_code.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

	* You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
	* You must use the packages urllib and sys
	* You are not allowed to import other packages than urllib and sys
	* You don’t need to check arguments passed to the script (number or type)
	* You must use the with statement
	* Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
```
[4. What's my status? #1](./4-hbtn_status.py)

Write a Python script that fetches https://alx-intranet.hbtn.io/status

	* You must use the package requests
	* You are not allow to import packages other than requests
	* The body of the response must be display like the following example (tabulation before -)

```
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
```

[5. Response header value #1](./5-hbtn_header.py)

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

	* You must use the packages requests and sys
	* You are not allow to import other packages than requests and sys
	* The value of this variable is different for each request
	* You don’t need to check script arguments (number and type)

```
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$ 

```

[6. POST an email #1](./6-post_email.py)

Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

	* The email must be sent in the variable email
	* You must use the packages requests and sys
	* You are not allowed to import packages other than requests and sys
	* You don’t need to error check arguments passed to the script (number or type)
	* Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 

```

[7. Error code #1](./7-error_code.py)

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

	* If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
	* You must use the packages requests and sys
	* You are not allowed to import packages other than requests and sys
	* You don’t need to check arguments passed to the script (number or type)
	* Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 

```
[8. Search API](./8-json_api.py)

Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

	* The letter must be sent in the variable q
	* If no argument is given, set q=""
	* If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
	* Otherwise:
		1. Display Not a valid JSON if the JSON is invalid
		2. Display No result if the JSON is empty
	* You must use the package requests and sys
	* You are not allowed to import packages other than requests and sys
Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.

```
guillaume@ubuntu:~/0x11$ ./8-json_api.py 
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
guillaume@ubuntu:~/0x11$ 

```

[9. My GitHub!](./10-my_github.py)

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

	* ou must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
	* The first argument will be your username
	* The second argument will be your password (in your case, a personal access token as password)
	* You must use the package requests and sys
	* You are not allowed to import packages other than requests and sys
	* You don’t need to check arguments passed to the script (number or type)

```
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
guillaume@ubuntu:~/0x11$ 

```

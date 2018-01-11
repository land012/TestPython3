# coding: utf-8

"""
web
"""
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', "text/html")])
    print(environ["REQUEST_METHOD"])
    print(environ["PATH_INFO"])
    print(environ["SCRIPT_NAME"])
    print(environ["QUERY_STRING"])
    return ["Hello World".encode(encoding="utf-8")]


if __name__ == "__main__":
    httpd = make_server('', 8080, application)
    print("Serving HTTP on port 8080.....")
    httpd.serve_forever()

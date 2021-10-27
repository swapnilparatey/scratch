# https://stackoverflow.com/questions/19434947/python-respond-to-http-request
# socketserver is part of the python library by default now - don't pip it
# BaseHTTPServer is now called http.server

import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer


def some_function():
    print("some functionn got called")


class MyHandler(BaseHTTPRequestHandler):
    # def __init__(self, request, client_address, server):
    #     BaseHTTPRequestHandler.__init__(self, request=self.request, client_address=self.client_address, server=self.server)
    #     self.count = 0

    # def get_count(self):
    #     self.count += 1
    #     return self.count

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

    def _html(self, message):
        content = "<html><body><h1>This is my " + message + "</h1></h2></body></html>\n"
        return content.encode("utf-8")

    def do_GET(self):
        self._set_headers()
        if self.path == '/captureImage':
            self.wfile.write(self._html("Reached capture image section"))
        if self.path == '/foobar':
            self.wfile.write((self._html("FOOBAR")))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        self.wfile.write("POST!!")


httpd = socketserver.TCPServer(("127.0.0.1", 8080), MyHandler)
httpd.serve_forever()
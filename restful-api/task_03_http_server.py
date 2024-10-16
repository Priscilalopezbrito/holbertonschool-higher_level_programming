#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(bytes(json.dumps(data), "utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(bytes(json.dumps(info), "utf-8"))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_m = {
                "error": "Not Found",
                "message": "Endpoint not found"
            }
            self.wfile.write(bytes(json.dumps(error_m), "utf-8"))


server = HTTPServer(('', 8000), MyHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
print("Server closed.")

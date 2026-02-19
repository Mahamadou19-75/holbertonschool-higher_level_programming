#!/usr/bin/python3
from task_03_http_server import SimpleAPIHandler
import http.server

if __name__ == "__main__":
    port = 8000
    server_address = ("", port)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    httpd.serve_forever()


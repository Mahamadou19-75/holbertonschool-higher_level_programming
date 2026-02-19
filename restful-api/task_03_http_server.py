#!/usr/bin/python3
import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests for simple API"""

        # ---- ROOT ENDPOINT ----
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # ---- /data ENDPOINT ----
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode())
            return

        # ---- /status ENDPOINT ----
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # ---- /info ENDPOINT ----
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.wfile.write(json.dumps(info).encode())
            return

        # ---- UNKNOWN ENDPOINT → 404 ----
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            return


if __name__ == "__main__":
    port = 8000
    server_address = ("", port)

    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


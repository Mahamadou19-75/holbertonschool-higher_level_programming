import http.server
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests for different endpoints."""

        # Root endpoint "/"
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # /data endpoint
        elif self.path == "/data":
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(sample_data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode())
            return

        # /status endpoint
        elif self.path == "/status":
            status = {"status": "OK"}
            json_status = json.dumps(status)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_status.encode())
            return

        # Undefined endpoint → 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            return


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server on port 8000."""
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()


#!/usr/bin/python3
"""
Simple API built using Python's http.server module
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Gestionnaire de requêtes personnalisé pour notre API simple
    """

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """
        Envoie les en-têtes HTTP
        """
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
        """
        Gère les requêtes GET
        """
        if self.path == "/":
            self._set_headers(200, "text/plain")
            self.wfile.write(
                b"Hello, this is a simple API!"
            )
        elif self.path == "/status":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")
        elif self.path == "/data":
            self._set_headers(200, "application/json")
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(
                json.dumps(data).encode("utf-8")
            )
        elif self.path == "/info":
            self._set_headers(200, "application/json")
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(
                json.dumps(info).encode("utf-8")
            )
        else:
            self._set_headers(404, "text/plain")
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Démarre le serveur HTTP
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

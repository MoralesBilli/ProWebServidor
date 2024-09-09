from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.get_response().encode("utf-8"))
            
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>Página no encontrada</h1>".encode("utf-8"))
            

    def get_response(self):
        try:
            
            with open('home.html', 'r') as file:
                return file.read()
        except Exception as e:
                return f"<h1>Error al cargar la página: {e}</h1>"


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()


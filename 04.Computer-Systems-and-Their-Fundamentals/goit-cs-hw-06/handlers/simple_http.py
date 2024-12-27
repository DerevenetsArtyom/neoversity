import os
import asyncio
import logging
import json
import mimetypes
import pathlib
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

import websockets

logging.basicConfig(level=logging.INFO)


HTTP_SERVER_HOST = os.getenv("HTTP_HOST")
HTTP_SERVER_PORT = int(os.getenv("HTTP_PORT"))

SOCKET_SERVER_HOST = os.getenv("SOCKET_HOST")
SOCKET_SERVER_PORT = int(os.getenv("SOCKET_PORT"))


class HttpHandler(BaseHTTPRequestHandler):
    """Class that handles all requests to HTTP server"""

    async def send_message(self, message: str):
        """Asynchronous function method that sends messages from HTTP to Socket server"""
        ws_resource_url = f"ws://{SOCKET_SERVER_HOST}:{SOCKET_SERVER_PORT}"
        async with websockets.connect(ws_resource_url) as websocket:
            await websocket.send(message)

    def do_POST(self):
        """Method that handles POST requests to the HTTP server"""
        url = urllib.parse.urlparse(self.path)

        if url.path != "/message":
            self.send_html_file("templates/error.html", 404)
            return

        data = self.rfile.read(int(self.headers["Content-Length"]))  # byte string
        data_parse = urllib.parse.unquote_plus(data.decode("utf-8"))  # decoded str
        data_dict = {
            key: value
            for key, value in [el.split("=") for el in data_parse.split("&")]
        }  # dict with parsed data

        asyncio.run(self.send_message(json.dumps(data_dict)))

        self.send_response(302)
        self.send_header("Location", "/")  # redirection to the main page
        self.end_headers()

    def do_GET(self):
        """Method that provides routing by handling GET requests to the HTTP server"""
        url = urllib.parse.urlparse(self.path)

        if url.path == "/":
            self.send_html_file("templates/index.html")
            return

        if url.path == "/message":
            self.send_html_file("templates/message.html")
            return

        if pathlib.Path().joinpath(url.path[1:]).exists():
            self.send_static()
            return

        self.send_html_file("templates/error.html", 404)

    def send_html_file(self, filename: str, status: int = 200):
        """Method that sends HTML files to the client as response from the HTTP server"""
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open(filename, "rb") as file:
            self.wfile.write(file.read())

    def send_static(self):
        """Method that sends static resources to the client"""
        self.send_response(200)

        mime_type = mimetypes.guess_type(self.path)
        if mime_type:
            self.send_header("Content-type", mime_type[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()

        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())


def run_http_server(server_class=HTTPServer, handler_class=HttpHandler):
    """Function to run HTTP server"""
    server_address = (HTTP_SERVER_HOST, HTTP_SERVER_PORT)
    http = server_class(server_address, handler_class)

    try:
        logging.info("HTTP server is running at 'http://%s:%s/'", HTTP_SERVER_HOST, HTTP_SERVER_PORT)
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()
        logging.info("HTTP server is interrupted")

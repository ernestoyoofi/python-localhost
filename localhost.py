# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<!DOCTYPE html><html><head><script src='https://code.jquery.com/jquery-3.6.0.js'></script></head>", "utf-8"))
        self.wfile.write(bytes("<body><script src='https://ernestoyoofi.github.io/python-localhost/render_chunk-82ba34cd-47hg12op.js'></script></body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started : http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
print("Server stopped.")
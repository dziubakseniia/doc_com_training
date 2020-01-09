import http.server
import socketserver


handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("server", 8004), handler) as httpd:
   httpd.serve_forever()

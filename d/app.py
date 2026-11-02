from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Employee Leave Management App Running")

print("Server started on port 5000", flush=True)
HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()

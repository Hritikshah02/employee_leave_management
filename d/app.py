from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Employee Leave Management App Running")

print("Server started on port 5000", flush=True)
HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()

# ---------------- STEPS (d) Containerization Using Docker ----------------
# 1. Write app.py and Dockerfile in this folder
# 2. docker build -t leave-app .
# 3. docker run -d --name leave-container -p 8080:5000 leave-app
# 4. docker ps                    (status: Up, port 8080->5000)
# 5. docker logs leave-container  (shows "Server started on port 5000")
# 6. curl localhost:8080 or open in browser
# 7. docker stop leave-container && docker rm leave-container (cleanup)

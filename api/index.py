from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/test":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response = {
                "message": "Vercel Python API is working 🚀"
            }

            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

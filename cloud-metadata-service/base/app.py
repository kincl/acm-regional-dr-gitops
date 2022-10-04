import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # print("Request headers:", self.headers)
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        
        metadata = {
            "cloudName": os.environ.get("CLOUDNAME") or "unknown",
            "zone": os.environ.get("ZONE") or "unknown"
        }
        self.wfile.write(bytes(json.dumps(metadata), "utf-8"))

def main():
    print('Listening on 0.0.0.0:8080')
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()

from http.server import HTTPServer, BaseHTTPRequestHandler
import time


HOST = "ip_your_computer"
PORT = random_free_port #type data int


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self. end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date: str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")

server.serve_forever()
server.server_close()
print("Server stopped!")


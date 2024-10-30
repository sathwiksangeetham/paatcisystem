import socketserver
import threading

class DispatcherHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"Received: {data}")
        self.request.sendall(b"OK")

def serve():
    server = socketserver.ThreadingTCPServer(("localhost", 8888), DispatcherHandler)
    print("Dispatcher running on localhost:8888")
    server.serve_forever()

if __name__ == "__main__":
    serve()


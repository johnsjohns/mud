import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_sockets = []
        self.lock = threading.Lock()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            self.client_sockets.append(client_socket)
            threading.Thread(target=self.client_thread, args=(client_socket, client_address)).start()

    def client_thread(self, client_socket, client_address):
        print(f"New connection from {client_address[0]}:{client_address[1]}")

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.broadcast(message)
                else:
                    self.remove_client(client_socket)
                    break
            except:
                self.remove_client(client_socket)
                break

    def remove_client(self, client_socket):
        self.client_sockets.remove(client_socket)
        client_socket.close()

    def broadcast(self, message):
        with self.lock:
            for client_socket in self.client_sockets:
                try:
                    client_socket.sendall(message.encode())
                except:
                    self.remove_client(client_socket)

if __name__ == "__main__":
    server = ChatServer("localhost", 1234)
    server.start()


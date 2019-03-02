import socket
import pickle


class Server:

    def __init__(self):
        self.port = 9090
        self.ip = None
        self.sock = None
        self.conn = None
        self.address = None

    def create_server(self):
        sock = socket.socket()
        while 1:
            try:
                sock.bind(('', self.port))
                print(self.port)
                break
            except PermissionError and OSError:
                self.port = self.port + 1

        sock.listen(1)
        self.sock = sock

    def connect(self):
        self.conn, self.address = self.sock.accept()

    def send(self, data):
        data = pickle.dumps(data)
        self.conn.send(data)

    def get(self, size):
        data = self.conn.recv(size)
        data = pickle.loads(data)
        return data




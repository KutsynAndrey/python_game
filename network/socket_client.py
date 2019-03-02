import socket
import pickle


class Client:

    def __init__(self, **kwargs):
        self.ip = kwargs['ip']
        self.port = kwargs['port']
        self.sock = socket.socket()

    def connect(self):
        print('port -', self.port)
        print('ip -', self.ip)
        self.sock.connect((self.ip, self.port))

    def send(self, data):
        data = pickle.dumps(data)
        self.sock.send(data)

    def get(self, size):
        data = self.sock.recv(size)
        data = pickle.loads(data)
        return data





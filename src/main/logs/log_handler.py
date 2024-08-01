import socket
import struct
import pickle
from loguru import logger


class SocketHandler:

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def write(self, message):
        record = message.record
        data = pickle.dumps(record)
        slen = struct.pack(">L", len(data))
        self.sock.send(slen + data)


logger.configure(handlers=[{"sink": SocketHandler('localhost', 9999)}])
logger.add('log_file.txt', rotation="2 MB")

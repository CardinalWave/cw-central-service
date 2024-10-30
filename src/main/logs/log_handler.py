import socket
import struct
import pickle
import time
from loguru import logger
from src.config.config import Config


class SocketHandler:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.connect()

    def connect(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                print(f"Connected to cw-log-trace[{self.host}:{self.port}]")
                break
            except (socket.error, ConnectionRefusedError) as e:
                print(f"Connection failed: {e} - cw-log-trace. Retrying in 5 seconds...")
                time.sleep(5)

    def __del__(self):
        self.sock.close()

    def write(self, message):
        try:
            record = message.record
            data = pickle.dumps(record)
            slen = struct.pack(">L", len(data))
            self.sock.send(slen + data)
        except (socket.error, BrokenPipeError) as e:
            print(f"Error sending data: {e} -  cw-log-trace. Reconnecting...")
            self.connect()
            self.write(message)


socket_handler = SocketHandler(Config.CW_LOG_TRACE_IP, int(Config.CW_LOG_TRACE_PORT))
logger.configure(handlers=[{"sink": socket_handler.write}])
logger.add('log_file.txt', rotation="2 MB")

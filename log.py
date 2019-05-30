import argparse
import socket
import json
import logging
import inspect
from functools import wraps

ADDRESS = "localhost"
PORT = 7777
CONNECTIONS = 10   

server_logger = logging.getLogger("chat.server")
client_logger = logging.getLogger("chat.client")

def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        outer_func = inspect.stack()[1][3]
        server_logger.debug(f'Function " {func.__name__}" is called into "{outer_func}"')
        client_logger.debug(f'Function " {func.__name__}" is called into "{outer_func}"')
        return func(*args, **kwargs)
    return call

@log
def get_server_socket(addr, port):
    s = socket.socket()
    s.bind((addr, port))
    s.listen(CONNECTIONS)
    return s

@log
def get_client_socket(addr, port):
    s = socket.socket()
    s.connect((addr, port))
    return s
















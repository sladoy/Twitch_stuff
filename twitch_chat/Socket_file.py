from Settings_file import HOST, PORT
import socket


def OpenSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
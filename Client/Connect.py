import socket
import asyncio
import hashlib
import threading
import pickle


def connect():
    sock = socket.socket()
    sock.connect(('192.168.203.130', 9099))
    return sock

def snd(data, msg, sock):
    sock.send(data.encode())
    sock.send(msg.encode())
    

def snd_byte(data, msg, sock):
    sock.send(data)
    sock.send(msg.encode())


def rec(sock):
    data = sock.recv(1024)
    return data

def close_sock(sock):
    sock.close()


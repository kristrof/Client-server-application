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
    #data = data.split(' ')
    #pas = data[1]
    #print(data[1])
    #pas = hashlib.md5(pas.encode())
    #pas = pas.decode(utf-8)
    #print (str(data[1]))
    #ata1 = data+msg
    sock.send(data.encode())
    sock.send(msg.encode())
    #print(data)
    #data = sock.recv(1024)
    #msg = sock.recv(1024)
   # print(data.decode('utf-8'), msg.decode('utf-8'))


def snd_byte(data, msg, sock):
    sock.send(data)
    sock.send(msg.encode())


def rec(sock):
    data = sock.recv(1024)
    return data

def close_sock(sock):
    sock.close()

#sock = connect()
#data1 = ('kris')
#pas = "123"
#pas = hashlib.md5(pas.encode())
#pas = pas.hexdigest()
#data1 = data1+" "+pas
#msg1 = " 1"
#snd(data1, msg1, sock)
#res = rec(sock)
#close_sock(sock)
#print(res)
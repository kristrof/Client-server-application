import socket

def connect():
    sock = socket.socket()
    sock.bind(('', 9099))
    sock.listen(1)
    con, addr = sock.accept()

    print ('connected', addr)
    return con

def rec(con):

    while True:
        data = con.recv(1024)
        msg = con.recv(1024)
        if data:
            break        
        #con.send(data.upper())
        #con.send(msg.upper())
    print(data)
    #con.close()
    return msg.decode('utf-8')+ data.decode('utf-8')


def snd(data,con):
    con.sendall(data.encode())

def snd_byte(data,con):
    con.sendall(data)
    

def conn_close(con):
    con.close()

import socket
import pickle
import cv2
import numpy as np
import sandboxify as sb

PORT = 60000
SERVER_ADDRESS = ('', PORT)
BUFFER_SIZE = 4096
ENCODING = 'latin1'

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sock.bind(SERVER_ADDRESS)
    sock.listen(1)
    print("waiting for client", SERVER_ADDRESS)
    return sock

def recvall(sock):
    buffer = []
    while True:
        packet = conn.recv(BUFFER_SIZE)
        if not packet:
            break            
        buffer.append(packet)
    
    print('data received', len(buffer))
    return pickle.loads(b"".join(buffer), encoding=ENCODING)

def display(im):
    colored = sb.sandboxify(im)
    cv2.imshow('sandbox', colored)
    return cv2.waitKey(1)

cv2.namedWindow('sandbox')
sock = connect()

while True:
    conn, address = sock.accept()
    print("client connected", address)
    try:
        curr = recvall(conn)
        k = display(curr)
        if k == 27:
            break
    except Exception as ex:
        print('error while receiving data', ex)    
    finally:
        conn.close()      

cv2.destroyAllWindows()






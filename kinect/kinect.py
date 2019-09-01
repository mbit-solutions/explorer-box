import sys
import socket
import pickle
import depth
import time
import numpy as np

def send(sock, data)
    data_string = pickle.dumps(data)
    sock.sendall(data_string)
    sock.close()

def get_depth(address, port, threshold_diff, reset):
    zeros = np.zeros((640, 480))
    prev = zeros
    i = 0
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, port))

        curr = depth.get_depth_image()

        if not np.array_equal(prev, zeros):
            diff = depth.get_diff(prev, curr)
            coords = np.where(diff > [threshold_diff])
            curr[coords] = prev[coords]

        if i == reset:
            curr = depth.get_depth_image()
            i = 0
            print('reset depth img')

        prev = np.copy(curr)
        send(sock, curr)
        i += 1
        time.sleep(0.25)

def main():    
    address = '127.0.0.1'
    port = 60000
    threshold_diff = 150
    reset = 25

    if len(sys.argv) == 5:
        address = sys.argv[1]
        port = sys.argv[2]
        threshold_diff = sys.argv[3]
        reset = sys.argv[4]
        
    get_depth(address, port, threshold_diff, reset)

main()

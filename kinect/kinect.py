import sys
import socket
import pickle
import depth
import time
import numpy as np

def get_depth(address, port, threshold_diff):
    prev = np.zeros((640, 480))
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, port))

        curr = depth.get_depth_image()
        diff = depth.get_diff(prev, curr)
        coords = np.where(diff > [threshold_diff])
        curr[coords] = prev[coords]
        prev = curr

        data_string = pickle.dumps(curr)
        sock.sendall(data_string)
        sock.close()
        time.sleep(0.5)

def main():    
    arguments = len(sys.argv)

    if arguments == 4:
        address = sys.argv[1]
        port = sys.argv[2]
        threshold_diff = sys.argv[3]
        get_depth(address, port, threshold_diff)

main()

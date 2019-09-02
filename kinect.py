import sys
import depth
import time
import numpy as np
import sandboxify as sb
import cv2

def get_depth(threshold_diff, reset):
    zeros = np.zeros((640, 480))
    prev = zeros
    i = 0
    while True:
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
        colored = sb.sandboxify(curr)
        cv2.imshow('sandbox', colored)
        key = cv2.waitKey(1)
        if key == 27:
            break
        
        i += 1
        time.sleep(0.25)      


def main():    
    threshold_diff = 150
    reset = 25

    if len(sys.argv) == 3:
        threshold_diff = int(sys.argv[1])
        reset = int(sys.argv[2])  

    cv2.namedWindow('sandbox')        
    get_depth(threshold_diff, reset)    
    cv2.destroyAllWindows()

main()

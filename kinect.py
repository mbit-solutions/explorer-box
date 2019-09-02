import sys
import depth
import time
import numpy as np
import sandboxify as sb
import cv2

IGNORE_MM = 900

def get_current():
    return depth.get_depth_image_mm()            

def get_depth(threshold_diff, ignore_px_qty):
    zeros = np.zeros((640, 480))
    prev = zeros
    prev_always = zeros
    reset_flag = False 
    while True:        
        im = get_current()
        curr = np.copy(im)
        curr[np.where(im < [IGNORE_MM])] = 0
        
        if np.array_equal(prev, zeros):
            prev = np.copy(im)
            prev_always = np.copy(im)

        if not np.array_equal(prev_always, zeros):
            diff = depth.get_diff(prev_always, curr)
            coords = np.where(diff > [threshold_diff])
            curr[coords] = prev_always[coords]
       
        coords_qty = len(np.where(im < [IGNORE_MM])[0])           
        if coords_qty < ignore_px_qty:
            print('reset coords', coords_qty)
            curr = im 
            prev = np.copy(im)   
        else:  
            print('take prev cords', coords_qty)          
            c = np.where(curr < [IGNORE_MM])
            curr[c] = prev[c]
            
        prev_always = np.copy(curr)
        
        colored = sb.sandboxify(curr)
        cv2.imshow('sandbox', colored)
        key = cv2.waitKey(1)
        if key == 27:
            break        
    
        time.sleep(0.05) 

def main():    
    threshold_diff = 40
    ignore_px_qty = 8000

    if len(sys.argv) == 3:
        threshold_diff = int(sys.argv[1])
        ignore_px_qty = int(sys.argv[2])        

    cv2.namedWindow('sandbox')        
    get_depth(threshold_diff, ignore_px_qty)    
    cv2.destroyAllWindows()

main()

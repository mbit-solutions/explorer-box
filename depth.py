import numpy as np
import freenect
import cv2

def pretty_depth(depth):    
    np.clip(depth, 0, 2**10 - 1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth

def pretty_depth_cv(depth):    
    return pretty_depth(depth)

def get_diff(prev, curr):
    prevsubtract = prev.astype(np.int16)
    currsubtract = curr.astype(np.int16)
    diff = currsubtract - prevsubtract
    diff[np.where(diff < 0)] *= -1
    return diff.astype(np.uint8)

def get_depth_image():
    return pretty_depth_cv(freenect.sync_get_depth()[0])
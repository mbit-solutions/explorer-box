import numpy as np
import freenect as fn

class Kinect:
    def get_depth_image_mm(self):
        return fn.sync_get_depth(0, fn.DEPTH_MM)[0]
    
    def get_depth_image_diff_mm(self, previous, current, threshold):
        p = previous.astype(np.int16)
        c = current.astype(np.int16)
        diff = c - p
        diff[np.where(diff < 0)] *= -1
        return np.where(diff > [threshold])        
        

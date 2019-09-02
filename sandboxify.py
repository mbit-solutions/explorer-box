import posterize as p
import numpy as np
import colorize as col
import contourize as cont
import cv2

def sandboxify( im ):
    im = cv2.resize(im,(1600,1200))    
    im = 255 - im
    im = cv2.GaussianBlur(im,(3,3),0)
    im = interp(im)
    posterized = p.posterize(np.copy(im),10)
    
    colored = col.colorize(np.copy(im))
    
    colored[np.where(im == [0])] = [255]

    cont.contourize(colored,posterized)
    return colored

def interp( im ):
    im = np.interp(im,(47,70),(0,255)).astype(np.uint8)
    return im

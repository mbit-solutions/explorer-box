import posterize as p
import numpy as np
import colorize as col
import contourize as cont
import cv2

def sandboxify( im ):      
    
    im = np.interp(im,(1000,1300),(0,255)).astype(np.uint8)   
    im = cv2.resize(im, (1600,1200))     
    im = 255 - im
    im = cv2.GaussianBlur(im,(3,3),0)
    posterized = p.posterize(np.copy(im),20)   
   
    colored = col.explorer_colorize(np.copy(posterized)) 
    colored = cv2.GaussianBlur(colored,(3,3),0)
    cont.contourize(colored,posterized)

    return colored

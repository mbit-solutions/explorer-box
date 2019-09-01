import cv2

def colorize( im ):
    return cv2.applyColorMap(im,cv2.COLORMAP_JET)